#定义字典字面量
"""{key:value,key:value,......,key:value}"""

#定义字典变量
"""my_dict={key: value,key: value,......,key:value}"""

#定义空字典
"""
方式1：my_dict={}
方式2：my_dict=dict()
"""

#定义字典
my_dict1={"誉镠":100,"南海十三郎":99,"周生":98}

#定义空字典
my_dict2={}
my_dict3=dict()
print(f"字典1的内容是：{my_dict1},类型：{type(my_dict1 )}")
print(f"字典1的内容是：{my_dict2},类型：{type(my_dict2 )}")
print(f"字典1的内容是：{my_dict3},类型：{type(my_dict3 )}")

#定义重复key的字典(不允许重复)
my_dict_repeat={"誉镠":100,"誉镠":100,"南海十三郎":99,"周生":98}
print(f"重复key的字典内容是：{my_dict_repeat }")

#从字典中基于key获取value
"""***不可以使用下标索引***"""
print(my_dict1['誉镠'])
print(my_dict1['南海十三郎'])
print(my_dict1['周生'])

#定义嵌套字典
my_dict={"誉镠": {'语文':100,'数学':100,'英语':100},
    "南海十三郎": {'语文':99,'数学':99,'英语':99},
         "周生": {'语文':98,'数学':98,'英语':97}}
print(my_dict['南海十三郎'])

#从嵌套字典中获取数据
"""看一下誉镠的语文信息"""
score=my_dict['誉镠']['语文']
print(f'誉镠的语文成绩是{score}')