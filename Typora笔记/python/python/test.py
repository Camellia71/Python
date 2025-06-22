import ast

# 原始字符串
str_data = "[12,34,56,78,98,10]"

# 将字符串转换为列表
list_data = ast.literal_eval(str_data)

print(list_data)  # 输出: [12, 34, 56, 78, 98, 10]