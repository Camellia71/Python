

# 随机森林模型预测无人机续航时间（使用真实数据）
import numpy as np
import pandas as pd
from itertools import product
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import joblib  # 用于保存和加载模型

# 1. 加载真实数据（替换为你的数据文件路径）
try:
    # 支持CSV或Excel格式
    # data = pd.read_csv("drone_flight_data.csv")  # 方法1：从CSV加载
    data = pd.read_excel("E:\张岐奕1\EPI\github\Python\\random forest\\random.xlsx")  # 方法2：从Excel加载
except FileNotFoundError:
    print("错误：未找到数据文件！请检查文件路径")
    exit()

# 检查数据是否包含必需的列
required_columns = ['temperature', 'altitude', 'environment_type', 'flight_time']
if not all(col in data.columns for col in required_columns):
    print("错误：数据文件缺少必需的列！需要包含：", required_columns)
    exit()

# 2. 数据预处理
print("\n数据预览（前5行）：")
print(data.head())

# 处理缺失值（如果有）
if data.isnull().sum().any():
    print("\n发现缺失值：")
    print(data.isnull().sum())
    data = data.dropna()  # 简单处理：删除包含缺失值的行
    print("已删除包含缺失值的行")

# 分离特征和目标变量
X = data[['temperature', 'altitude', 'environment_type']]
y = data['flight_time']

# 3. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
)
print(f"\n数据集划分：训练集 {X_train.shape[0]} 条，测试集 {X_test.shape[0]} 条")

# 4. 创建预处理和建模管道
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', ['temperature', 'altitude']),  # 数值特征直接保留
        ('cat', OneHotEncoder(), ['environment_type'])  # 分类变量进行独热编码
    ])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1  # 使用所有CPU核心加速训练
    ))
])

# 5. 训练模型
print("\n开始训练模型...")
model.fit(X_train, y_train)
print("模型训练完成！")

# 6. 模型评估
y_pred = model.predict(X_test)

print("\n模型评估指标：")
print(f"- 平均绝对误差(MAE): {mean_absolute_error(y_test, y_pred):.2f} 分钟")
print(f"- 均方误差(MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"- 均方根误差(RMSE): {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} 分钟")
print(f"- R²分数: {r2_score(y_test, y_pred):.2f}")

# 7. 特征重要性分析
# 获取特征名称（包括独热编码后的类别特征）
numeric_features = ['temperature', 'altitude']
categorical_features = model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(['environment_type'])
feature_names = numeric_features + list(categorical_features)

importances = model.named_steps['regressor'].feature_importances_

print("\n特征重要性排序：")
for name, importance in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
    print(f"{name}: {importance:.4f}")

# 可视化特征重要性
plt.figure(figsize=(10, 5))
plt.barh(feature_names, importances)
plt.xlabel("Importance Score")
plt.title("Feature Importance")
plt.gca().invert_yaxis()  # 重要性从高到低显示
plt.tight_layout()
plt.savefig("feature_importance.png")  # 保存图表
print("\n已保存特征重要性图表：feature_importance.png")

# 8. 保存模型
joblib.dump(model, "drone_flight_time_predictor.pkl")
print("\n已保存训练好的模型：drone_flight_time_predictor.pkl")


from itertools import product
# 9. 使用模型进行新数据预测
temperatures = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
altitudes = [0, 500, 1000, 1500, 2000, 2500, 3000]
environments = ['urban', 'forest', 'grassland']

# 生成所有组合
combinations = list(product(temperatures, altitudes, environments))
new_data = pd.DataFrame(combinations, columns=['temperature', 'altitude', 'environment_type'])

# 预测并打印结果
predicted_times = model.predict(new_data)
print("\n新数据预测结果（前10条）：")
for i in range(10):  # 仅显示前10条结果
    row = new_data.iloc[i]
    print(f"组合{i+1}: 温度={row['temperature']}℃, 海拔={row['altitude']}m, 环境={row['environment_type']} → 预测续航: {predicted_times[i]:.1f} 分钟")

# 保存所有预测结果到CSV（可选）
results = new_data.copy()
results['predicted_flight_time'] = predicted_times
results.to_csv("all_predictions.csv", index=False)
print("\n已保存所有预测结果到: all_predictions.csv")