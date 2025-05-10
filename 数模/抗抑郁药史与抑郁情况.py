import pandas as pd
import matplotlib.pyplot as plt


def process_antidepressant_depression(file_path):
    # ================== 数据读取 ==================
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        print("✅ 数据读取成功！前3行数据预览：")
        print(df.head(3))
    except Exception as e:
        print(f"❌ 文件读取失败: {str(e)}")
        return

    # ================== 数据清洗 ==================
    try:
        # 定义关键列
        antidepressant_cols = ['无', '使用过抗抑郁药', '其它']
        depression_cols = ['轻度', '中度', '重度']

        # 处理空白和非数字字符
        for col in antidepressant_cols + depression_cols:
            # 转为字符串处理特殊字符
            df[col] = df[col].astype(str).str.strip().replace({'': '0', 'nan': '0'})
            # 安全转换为数值
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            # 最终转为整数
            df[col] = df[col].astype(int)

        # 提取有效标记数据
        def get_category(row, cols):
            if row[cols].sum() == 1:
                return row[cols].idxmax()
            return None

        df['抗抑郁药史'] = df.apply(lambda x: get_category(x, antidepressant_cols), axis=1)
        df['抑郁程度'] = df.apply(lambda x: get_category(x, depression_cols), axis=1)

        # 过滤无效数据
        invalid_data = df[df[['抗抑郁药史', '抑郁程度']].isnull().any(axis=1)]
        df = df.dropna(subset=['抗抑郁药史', '抑郁程度']).copy()
        print(f"🔄 数据清洗完成，有效数据：{len(df)}条，排除无效数据：{len(invalid_data)}条")

    except Exception as e:
        print(f"❌ 数据处理失败: {str(e)}")
        return

    # ================== 可视化分析 ==================
    try:
        # 按组别生成图表
        for group in df['组别'].unique():
            group_df = df[df['组别'] == group]

            # 创建交叉表
            cross_tab = pd.crosstab(
                index=group_df['抗抑郁药史'],
                columns=group_df['抑郁程度'],
                colnames=[None]
            )[depression_cols]  # 固定列顺序

            # 配置图表
            plt.figure(figsize=(12, 6))
            ax = cross_tab.plot.bar(
                rot=0,
                color=['#66c2a5', '#fc8d62', '#8da0cb'],
                edgecolor='black',
                width=0.8
            )

            # 图表装饰
            plt.title(f'组别 {group} - 抗抑郁药史与抑郁程度关系\n',
                      fontsize=14, pad=20, fontweight='bold')
            plt.xlabel('抗抑郁药史', fontsize=12, labelpad=15)
            plt.ylabel('人数', fontsize=12, labelpad=15)
            plt.xticks(fontsize=10, rotation=45, ha='right')

            # 添加数据标签
            for container in ax.containers:
                ax.bar_label(
                    container,
                    fmt='%d',
                    label_type='edge',
                    padding=5,
                    fontsize=9
                )

            # 调整布局并保存
            plt.tight_layout()
            plt.savefig(f'组别{group}_抗抑郁药史分析.png',
                        dpi=300,
                        bbox_inches='tight')
            plt.close()
            print(f"📊 已生成组别 {group} 的分析图表")

    except Exception as e:
        print(f"❌ 可视化生成失败: {str(e)}")
        return

    # ================== 生成报告 ==================
    try:
        # 保存清洗后的数据
        df.to_excel('清洗后数据.xlsx', index=False)
        print("💾 已保存清洗后的数据文件：清洗后数据.xlsx")

        # 生成总报告
        total_report = pd.crosstab(
            index=df['抗抑郁药史'],
            columns=df['抑郁程度'],
            margins=True,
            margins_name="总计"
        )
        total_report.to_excel('总体分析报告.xlsx')
        print("📈 已生成总体分析报告")

    except Exception as e:
        print(f"⚠️ 报告生成失败: {str(e)}")

    print("🎉 处理流程全部完成！")


# ================== 运行配置 ==================
if __name__ == "__main__":
    # 中文字体配置
    plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统
    # plt.rcParams['font.sans-serif'] = ['PingFang HK']  # Mac系统
    plt.rcParams['axes.unicode_minus'] = False

    # 执行分析
    process_antidepressant_depression("data.xlsx")  # 替换为实际文件路径