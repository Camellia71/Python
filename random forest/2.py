import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

# 1. 模拟生成一些示例数据（在实际应用中，你应该使用真实数据）
np.random.seed(42)
n_samples = 1000

# 生成特征数据
temperature = np.random.uniform(-10, 40, n_samples)  # 温度范围-10到40摄氏度
altitude = np.random.uniform(0, 3000, n_samples)     # 海拔范围0到3000米
environment_types = np.random.choice(['urban', 'rural', 'mountain', 'coastal'], n_samples)  # 环境类型

# 生成目标变量（续航时间，范围5-46分钟）
# 假设温度适中、海拔低、urban环境时续航时间最长
base_time = 46
time_reduction = (
    np.abs(temperature - 25) * 0.2 +  # 偏离最佳温度(20°C)的影响
    altitude * 0.005 +                # 海拔影响
    np.where(environment_types == 'urban', 5, 
             np.where(environment_types == 'mountain', 10, 
                     np.where(environment_types == 'coastal', 8, 3)))  # 环境类型影响
)

flight_time = np.clip(base_time - time_reduction + np.random.normal(0, 2, n_samples), 5, 46)

# 创建DataFrame
data = pd.DataFrame({
    'temperature': temperature,
    'altitude': altitude,
    'environment_type': environment_types,
    'flight_time': flight_time
})

# 2. 数据预处理
# 分离特征和目标变量
X = data.drop('flight_time', axis=1)
y = data['flight_time']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 预处理管道：对环境类型进行独热编码，数值特征保持不变
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', ['temperature', 'altitude']),
        ('cat', OneHotEncoder(), ['environment_type'])
    ])

# 3. 创建随机森林模型管道
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# 4. 训练模型
model.fit(X_train, y_train)

# 5. 模型评估
y_pred = model.predict(X_test)

print("模型评估指标:")
print(f"平均绝对误差(MAE): {mean_absolute_error(y_test, y_pred):.2f} 分钟")
print(f"均方误差(MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"均方根误差(RMSE): {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} 分钟")
print(f"R²分数: {r2_score(y_test, y_pred):.2f}")

# 6. 特征重要性分析
# 获取特征名称（包括独热编码后的类别特征）
numeric_features = ['temperature', 'altitude']
categorical_features = model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(['environment_type'])
feature_names = np.concatenate([numeric_features, categorical_features])

# 获取特征重要性
importances = model.named_steps['regressor'].feature_importances_
indices = np.argsort(importances)[::-1]

# 打印特征重要性
print("\n特征重要性:")
for f in range(X_train.shape[1]):
    print(f"{feature_names[indices[f]]}: {importances[indices[f]]:.4f}")

# 可视化特征重要性
plt.figure(figsize=(10, 6))
plt.title("特征重要性")
plt.bar(range(X_train.shape[1]), importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), feature_names[indices], rotation=45)
plt.tight_layout()
plt.show()

# 7. 实际预测示例
new_data = pd.DataFrame({
    'temperature': [25, 10, -5],
    'altitude': [100, 1500, 2500],
    'environment_type': ['urban', 'mountain', 'rural']
})

predicted_times = model.predict(new_data)
print("\n预测续航时间:")
for i, time in enumerate(predicted_times):
    print(f"情况{i+1}: {time:.1f} 分钟")