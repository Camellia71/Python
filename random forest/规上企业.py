import pandas as pd
import numpy as np
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value

# 数据准备
data = pd.read_excel("data_p.xlsx")
# 删除nan行
data = data.dropna()

# 按名称分组处理
grouped = data.groupby('行业')
results = []

for name, group in grouped:
    df = pd.DataFrame(group)
    # 定义输入和输出变量
    inputs = df[["投入_人力投入", "投入_R&D科技活动经费支出", "投入_新产品开发经费支出", "投入_新产品开发项目数"]]
    outputs = df[["产出_专利受理数件", "产出_有效发明专利数", "产出_新产品销售收入", "产出_新产品出口收入"]]

    # DEA函数
    def dea_analysis(inputs, outputs, returns="CRS"):
        """
        数据包络分析(DEA)效率计算函数（乘数形式）

        参数：
        inputs : DataFrame  - 输入指标矩阵（每行代表一个DMU）
        outputs : DataFrame - 输出指标矩阵（每行代表一个DMU）
        returns : str       - 模型类型，"CRS"（默认）或"VRS"

        返回：
        list - 各DMU的效率得分（0~1之间）
        """

        n = inputs.shape[0]  # 决策单元数量
        m = inputs.shape[1]  # 输入指标数
        s = outputs.shape[1]  # 输出指标数

        efficiency_scores = []

        for i in range(n):
            prob = LpProblem(f"DEA_DMU_{i}", LpMaximize)

            # 定义变量
            u = [LpVariable(f"u_{j}", lowBound=0) for j in range(s)]  # 输出权重
            v = [LpVariable(f"v_{j}", lowBound=0) for j in range(m)]  # 输入权重

            # VRS模型需要截距项
            if returns == "VRS":
                u0 = LpVariable("u0", cat="Free")  # 自由变量（可正可负）

            # 目标函数：最大化当前DMU的效率
            if returns == "VRS":
                prob += lpSum(u[j] * outputs.iloc[i, j] for j in range(s)) + u0
            else:
                prob += lpSum(u[j] * outputs.iloc[i, j] for j in range(s))

            # 归一化约束：输入权重和为1
            prob += lpSum(v[j] * inputs.iloc[i, j] for j in range(m)) == 1

            # 效率约束：所有DMU的效率<=1
            for k in range(n):
                if returns == "VRS":
                    constraint = (lpSum(u[j] * outputs.iloc[k, j] for j in range(s)) -
                                  lpSum(v[j] * inputs.iloc[k, j] for j in range(m)) + u0 <= 0)
                else:
                    constraint = (lpSum(u[j] * outputs.iloc[k, j] for j in range(s)) -
                                  lpSum(v[j] * inputs.iloc[k, j] for j in range(m)) <= 0)
                prob += constraint

            # 求解并获取结果
            prob.solve()
            eff_score = value(prob.objective) if returns == "VRS" else value(prob.objective)
            efficiency_scores.append(round(eff_score, 4))

        return efficiency_scores

    # 计算技术效率（CRS模型）
    crs_efficiency = dea_analysis(inputs, outputs, returns="CRS")

    # 计算纯技术效率（VRS模型）
    vrs_efficiency = dea_analysis(inputs, outputs, returns="VRS")

    # 计算规模效率
    scale_efficiency = [crs / vrs if vrs > 0 else 0 for crs, vrs in zip(crs_efficiency, vrs_efficiency)]

    # 将结果添加到DataFrame中
    df["技术效率"] = crs_efficiency
    df["纯技术效率"] = vrs_efficiency
    df["规模效率"] = scale_efficiency


    results.append(df[["行业", "年份", "技术效率", "纯技术效率", "规模效率"]])

# 合并所有结果
final_result = pd.concat(results)
final_result["规模效率"]  =final_result['技术效率'] / final_result['纯技术效率'] 
# 打印结果
print(final_result)
## 预测代码
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

# 读取数据
data = pd.read_csv('合并数据1.csv', encoding='gbk')

# 数据预处理
def preprocess_data(data):
    # 提取特征和目标变量
    industries = data['名称'].unique()
    all_predictions = {}
    for industry in industries:
        industry_data = data[data['名称'] == industry].drop(['名称', '年份'], axis=1)
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(industry_data)

        # 准备训练数据
        X, y = [], []
        for i in range(len(scaled_data) - 3):
            X.append(scaled_data[i:i + 3])
            y.append(scaled_data[i + 3])
        X = np.array(X)
        y = np.array(y)

        # 构建 LSTM 模型
        model = Sequential()
        model.add(LSTM(50, activation='relu', input_shape=(3, X.shape[2])))
        model.add(Dense(X.shape[2]))
        model.compile(optimizer='adam', loss='mse')

        # 训练模型
        early_stopping = EarlyStopping(patience=10, restore_best_weights=True)
        model.fit(X, y, epochs=100, batch_size=1, verbose=1, callbacks=[early_stopping])

        # 预测未来三年
        last_sequence = scaled_data[-3:]
        future_predictions = []
        for _ in range(3):
            next_prediction = model.predict(last_sequence.reshape(1, 3, X.shape[2]))
            future_predictions.append(next_prediction[0])
            last_sequence = np.vstack((last_sequence[1:], next_prediction))

        # 反归一化
        future_predictions = scaler.inverse_transform(future_predictions)
        all_predictions[industry] = future_predictions

    return all_predictions


# 进行预测
predictions = preprocess_data(data)

# 打印结果为表格
for industry, preds in predictions.items():
    print(f"行业: {industry}")
    columns = data.columns.drop(['名称', '年份'])
    future_years = [f"未来第 {i + 1} 年" for i in range(3)]
    df = pd.DataFrame(preds, columns=columns, index=future_years)
    print(df)
    print()
    
