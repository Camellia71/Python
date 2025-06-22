"""
演示JSON数据和python字典的相互转换
"""
import json

#准备列表，列表内每一个元素都是字典，将其转换为JSON
date=[{'name':'张三','age':11},{'name':'李四','age':13},{'name':'王五','age':16}]
json_str=json.dumps(date,ensure_ascii=False)
print(type(json_str))
print(json_str)

#准备字典，将字典转换为JSON
d={'name':'周杰伦','adress':'台北'}
json_str=json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)

#将JSON字符串转换为Python数据类型{k:v,k:v},{k:v,k:v}
s='[{"name":"张三","age":11},{"name":"李四","age":13},{"name":"王五","age":16}]'
l=json.loads(s)
print(type(l))
print(l)