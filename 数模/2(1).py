import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans']  # 支持中文和符号的字体
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# 设置中文显示和样式
sns.set(style="whitegrid", font='SimHei')
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def load_and_preprocess(file_paths):
    """增强型数据预处理"""
    dfs = []
    for file in file_paths:
        try:
            df = pd.read_excel(file, engine='openpyxl')

            # 统一列名格式（处理特殊字符和空格）
            df.columns = df.columns.str.replace(r'[^a-zA-Z0-9\u4e00-\u9fa5]', '', regex=True)

            # 关键字段校验
            required_cols = ['未婚', '已婚', '离异', '丧偶',
                             '无', '使用过抗抑郁药', '其它',
                             '轻度', '中度', '重度',
                             '主诉情况合计']
            missing = [col for col in required_cols if col not in df.columns]
            if missing:
                print(f"文件 {file} 缺少必要列：{missing}")
                continue

            # 类型转换
            for col in required_cols[:-1]:  # 分类列转换为整型
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(np.int8)
            df['主诉情况合计'] = pd.to_numeric(df['主诉情况合计'], errors='coerce').fillna(0).astype(np.int16)

            dfs.append(df)

        except Exception as e:
            print(f"处理文件 {file} 失败: {str(e)}")
            continue

    if not dfs:
        raise ValueError("没有有效数据可供分析")

    return pd.concat(dfs, ignore_index=True)


def analyze_effects(df):
    """增强型统计分析"""
    # 生成特征
    df['婚姻状态'] = df[['未婚', '已婚', '离异', '丧偶']].idxmax(axis=1)
    df['用药历史'] = df[['无', '使用过抗抑郁药', '其它']].idxmax(axis=1)
    df['抑郁程度'] = df[['轻度', '中度', '重度']].idxmax(axis=1)

    # 创建哑变量并确保数值类型
    dummies = pd.get_dummies(
        df[['婚姻状态', '用药历史', '抑郁程度']],
        drop_first=True
    ).astype(np.int8)

    X = sm.add_constant(dummies)
    y = df['主诉情况合计'].astype(np.int16)

    # 模型拟合
    print("\n正在拟合负二项回归模型...")
    model = sm.GLM(y, X,
                   family=sm.families.NegativeBinomial(
                       alpha=1.0  # 显式设置离散参数
                   ))
    results = model.fit()

    # 结果输出
    print("\n=== 模型统计结果 ===")
    print(results.summary())

    # 可视化
    coefs = results.params[1:]
    conf_int = results.conf_int().iloc[1:]

    plt.figure(figsize=(10, 6))
    sns.pointplot(x=np.exp(coefs), y=coefs.index,
                  linestyle='none',  # 替换弃用的join参数
                  color='black', markers='o', scale=0.8)
    plt.errorbar(x=np.exp(coefs), y=coefs.index,
                 xerr=[np.exp(coefs) - np.exp(conf_int[0]),
                       np.exp(conf_int[1]) - np.exp(coefs)],
                 fmt='o', color='darkblue')
    plt.axvline(1, color='red', linestyle='--')
    plt.xscale('log')
    plt.title('各因素对主诉情况的影响效应（IRR）', fontsize=14)
    plt.xlabel('发生率比（对数尺度）', fontsize=12)
    plt.tight_layout()
    plt.savefig('analysis_result.png', dpi=300)
    print("\n分析结果已保存至 analysis_result.png")


if __name__ == "__main__":
    try:
        # 自动查找数据文件
        data_dir = Path.cwd()
        data_files = [
            f for f in data_dir.glob('*.xlsx')
            if any(kw in f.name for kw in ['随访', '主诉'])
        ]

        if not data_files:
            raise FileNotFoundError("未找到符合要求的Excel文件（文件名需包含'随访'或'主诉'）")

        # 预处理数据
        df = load_and_preprocess(data_files)

        # 执行分析
        analyze_effects(df)

    except Exception as e:
        print(f"\n发生错误：{str(e)}")
        print("可能的原因：")
        print("1. Excel文件未包含必要列（详见上述提示）")
        print("2. 数据格式不正确（需为数值型）")
        print("3. 文件损坏或受密码保护")
        print(f"当前工作目录：{data_dir}")