import pandas as pd
import statsmodels.api as sm

# 读取数据（假设数据已加载为 DataFrame，文件路径需替换）
df = pd.read_excel("一院随访的抗抑郁药物使用后主诉情况(2).xlsx", sheet_name="一院临床受试者及抑郁症的基本数据")

# 数据预处理（示例，需根据实际列名调整）
# 婚姻状况：选择 "未婚" 作为参考类别，生成哑变量（已存在则直接使用）
df["婚姻状况"] = df[["未婚", "已婚", "离异", "丧偶"]].idxmax(axis=1)  # 合并为单列分类变量
marital_dummies = pd.get_dummies(df["婚姻状况"], prefix="婚姻", drop_first=True)  # 哑变量化

# 既往用药史：选择 "无" 作为参考类别
med_history_dummies = pd.get_dummies(df["既往抗抑郁药使用情况"], prefix="用药史", drop_first=True)

# 初始抑郁程度：选择 "轻度" 作为参考类别
depression_dummies = pd.get_dummies(df["抑郁程度"], prefix="抑郁程度", drop_first=True)

# 合并自变量（假设因变量为虚构的 "疗效评分"，需替换为真实数据）
X = pd.concat([marital_dummies, med_history_dummies, depression_dummies], axis=1)
y = df["疗效评分"]  # 假设存在该列

# 添加常数项
X = sm.add_constant(X)

# 多元线性回归
model = sm.OLS(y, X).fit()
print(model.summary())

# 输出关键影响因素（p<0.05）
significant_vars = model.pvalues[model.pvalues < 0.05].index.tolist()
print("\n显著影响因素:", significant_vars)