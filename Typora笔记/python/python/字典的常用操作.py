my_dict={"誉镠":100,"南海十三郎":99,"周生":98}

#新增元素
"""语法：字典[Key]=Value,结果：字典被修改，新增元素"""
my_dict["富生"]=97
print(my_dict )

#更新元素
"""语法：字典.[Key]=Value,结果：字典被修改，元素被更新"""
my_dict ['南海十三郎']=66
print(my_dict )

#删除元素
"""语法：字典.pop(Key),结果：获得指定Key的Value,同时字典被修改，指定key的数据被删改"""
value=my_dict.pop('富生')
print(value)
print(my_dict )

#清空元素
"""字典.clear(),结果：字典被修改，元素被清空"""
my_dict.clear()
print(my_dict)

#获取全部key
"""语法:字典.keys(),结果：得到字典中的全部key"""
my_dict={"誉镠":100,"南海十三郎":99,"周生":98}
keys=my_dict.keys()
print(keys)

#遍历字典
for key in keys:
    print(f'字典的key是:{key}')
    print(f'字典的value是：{my_dict [key]}')

for key in my_dict :
    print(f'字典的key是:{key}')
    print(f'字典的value是：{my_dict[key]}')

#统计内元素数量len()函数
length=len(my_dict )
print(length)