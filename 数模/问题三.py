import pandas as pd
import numpy as np


def read_hospital_data(data, hospital_name):
    """带数据清洗的医院数据读取"""
    metrics = {
        '失访': ['失访1', '失访3', '失访6', '失访12'],  # 保留用于计算有效分母
        '失眠': ['失眠1', '失眠3', '失眠6', '失眠12'],
        '脱发': ['脱发1', '脱发3', '脱发6', '脱发12'],
        '激素水平异常': ['激素水平异常1', '激素水平异常3', '激素水平异常6', '激素水平异常12'],
        '嗜睡': ['嗜睡1', '嗜睡3', '嗜睡6', '嗜睡12'],
        '便秘': ['便秘1', '便秘3', '便秘6', '便秘12']
    }

    # 数据标准化处理
    for cols in metrics.values():
        for c in cols:
            data[c] = np.where(data[c].astype(str).str.contains('1'), 1, 0)

    # 转换宽表为长格式
    melted_dfs = []
    for metric, cols in metrics.items():
        df = data[['序号', '组别'] + cols].copy()
        df = df.melt(id_vars=['序号', '组别'],
                     value_vars=cols,
                     var_name='时间',
                     value_name=metric)
        df['时间'] = df['时间'].str.extract(r'(\d+)').astype(int)  # 添加r前缀
        melted_dfs.append(df.set_index(['序号', '组别', '时间']))

    combined = pd.concat(melted_dfs, axis=1).reset_index()
    combined['医院'] = hospital_name
    return combined


def calculate_effective_denominator(df):
    """计算有效病例分母（考虑失访情况）"""
    # 获取每个患者的最后有效时间点
    lost_times = df.groupby(['序号', '组别', '医院'])['时间'].max().reset_index()
    lost_times.rename(columns={'时间': '最后有效时间'}, inplace=True)

    # 生成所有可能的时间点
    all_times = pd.DataFrame({'时间': [1, 3, 6, 12]})

    # 合并生成有效观察矩阵
    return pd.merge(
        df[['序号', '组别', '医院']].drop_duplicates()
        .merge(all_times, how='cross'),
        lost_times,
        how='left'
    ).query('时间 <= 最后有效时间')


def analyze_symptoms(df):
    """症状指标分析"""
    # 获取有效观察窗口
    valid_obs = calculate_effective_denominator(df)

    # 定义分析指标
    symptoms = ['失眠', '脱发', '激素水平异常', '嗜睡', '便秘']

    # 合并症状数据
    symptom_data = valid_obs.merge(
        df[['序号', '组别', '医院', '时间'] + symptoms],
        how='left'
    )

    # 按维度聚合分析
    analysis = (
        symptom_data.groupby(['医院', '组别', '时间'])
        .agg(
            denominator=('序号', 'nunique'),
            **{f'{sym}_rate': (sym, 'mean') for sym in symptoms}
        )
        .reset_index()
    )

    # 转换结果格式
    melted = analysis.melt(
        id_vars=['医院', '组别', '时间', 'denominator'],
        value_vars=[f'{sym}_rate' for sym in symptoms],
        var_name='症状',
        value_name='发生率'
    )

    # 格式优化
    melted['症状'] = melted['症状'].str.replace('_rate', '')
    melted['发生率'] = (melted['发生率'] * 100).round(2)

    return melted.pivot_table(
        index=['时间', '症状'],
        columns=['医院', '组别'],
        values='发生率',
        aggfunc='first'
    ).fillna(0)


# 使用示例
hospital1_data = pd.read_excel("两个医院随访的抗抑郁药使用后主诉情况.xlsx", sheet_name="一院随访的抗抑郁药物使用后主诉情况")
hospital2_data = pd.read_excel("两个医院随访的抗抑郁药使用后主诉情况.xlsx", sheet_name="二院随访的抗抑郁药物使用后主诉情况")

df_h1 = read_hospital_data(hospital1_data, '一院')
df_h2 = read_hospital_data(hospital2_data, '二院')
combined_df = pd.concat([df_h1, df_h2])

result = analyze_symptoms(combined_df)
print(result)