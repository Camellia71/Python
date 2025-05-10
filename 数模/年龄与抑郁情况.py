import pandas as pd
import matplotlib.pyplot as plt


def process_and_visualize(file_path):
    # 读取数据
    try:
        df = pd.read_excel(file_path)
        print("数据读取成功！前3行数据预览：")
        print(df.head(3))
    except Exception as e:
        print(f"文件读取失败: {str(e)}")
        return

    # 数据清洗和转换
    try:
        # 转换数值列
        df[['轻度', '中度', '重度']] = df[['轻度', '中度', '重度']].apply(pd.to_numeric, errors='coerce').fillna(0)

        # 转换长格式
        df_long = pd.melt(
            df,
            id_vars=['序号', '组别', '年龄'],
            value_vars=['轻度', '中度', '重度'],
            var_name='抑郁程度',
            value_name='人数'
        )

        # 关键修复：调整年龄分段区间
        bins = [20, 25, 30, 35, 41]  # 扩大最后一个区间上限
        labels = ['20-24岁', '25-29岁', '30-34岁', '35-40岁']

        df_long['年龄段'] = pd.cut(
            df_long['年龄'],
            bins=bins,
            labels=labels,
            right=False  # 左闭右开 [20,25) [25,30)...[35,41)
        )

        # 仅过滤无效分段数据（保留20-40岁）
        df_long = df_long[df_long['年龄段'].notna()].copy()

    except Exception as e:
        print(f"数据处理失败: {str(e)}")
        return

    # 按组别生成图表（代码保持不变）
    for group in df_long['组别'].unique():
        group_df = df_long[df_long['组别'] == group]

        pivot_table = group_df.pivot_table(
            index='年龄段',
            columns='抑郁程度',
            values='人数',
            aggfunc='sum',
            fill_value=0,
            observed=True
        ).reindex(labels, fill_value=0)

        plt.figure(figsize=(10, 6))
        ax = pivot_table.plot.bar(
            rot=45,
            color=['#66c2a5', '#fc8d62', '#8da0cb'],
            width=0.8
        )

        plt.title(f'组别 {group} - 抑郁程度分布', fontsize=14)
        plt.xlabel('')
        plt.ylabel('人数', fontsize=12)

        for container in ax.containers:
            ax.bar_label(container, fmt='%d', padding=3)

        plt.tight_layout()
        plt.savefig(f'组别{group}_分析.png', dpi=300)
        plt.close()

    print("处理完成，请查看生成的PNG文件")


# 运行配置
if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    process_and_visualize("data.xlsx")