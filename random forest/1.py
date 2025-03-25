import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 生成模拟数据，实际应用中请替换为真实数据
data = {
    'altitude': [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000] * 5,
    'temperature': [10, 15, 20, 25, 30] * 8,
    'flight_time': [43.7, 41.4, 39.1, 36.8, 34.5, 32.2, 29.9, 27.6] * 5  # 模拟续航时间
}
df = pd.DataFrame(data)

# 特征矩阵 X 和目标变量 y
X = df[['altitude', 'temperature']]
y = df['flight_time']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建随机森林回归模型
model = RandomForestRegressor(n_estimators=100, random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差: {mse}")

# 新数据预测
new_data = pd.DataFrame({
    'altitude': [2200],
    'temperature': [22]
})
predicted_flight_time = model.predict(new_data)
print(f"预测的续航时间: {predicted_flight_time[0]} 分钟")