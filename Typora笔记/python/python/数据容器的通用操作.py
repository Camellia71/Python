#遍历
"""
①5类数据容器都支持for循环
②列表、元组、字符串支持while循环，集合、字典不支持(无法下标索引)
"""
my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str='南海十三郎江誉镠'
my_set={1,2,3,4,5}
my_dict={'key1':'程蝶衣','key2':'段小楼','key3':'柯南','key4':'灰原哀'}

#len元素个数
print(f'元素个数为：{len(my_list)}')
print(f'元素个数为：{len(my_tuple)}')
print(f'元素个数为：{len(my_str)}')
print(f'元素个数为：{len(my_set)}')
print(f'元素个数为：{len(my_dict)}')

print('\n')

#max最大元素(max()函数)
print(f'最大元素为：{max(my_list)}')
print(f'最大元素为：{max(my_tuple)}')
print(f'最大元素为：{max(my_str)}')
print(f'最大元素为：{max(my_set)}')
print(f'最大元素为：{max(my_dict)}')

print('\n')

#min最小元素(min())
print(f'最小元素为：{min(my_list)}')
print(f'最小元素为：{min(my_tuple)}')
print(f'最小元素为：{min(my_str)}')
print(f'最小元素为：{min(my_set)}')
print(f'最小元素为：{min(my_dict)}')

print('\n')

#类型转换：容器转列表
"""语法：list(容器) str(容器) tuple(容器) set(容器)"""
print(f'列表转列表的结果是：{list(my_list)}')
print(f'元组转列表的结果是：{list(my_tuple)}')
print(f'字符串转列表结果是：{list(my_str)}')
print(f'集合转列表的结果是：{list(my_set)}')
print(f'字典转列表的结果是：{list(my_dict)}')

print('\n')

#类型转换：容器转元组
"""语法：list(容器) str(容器) tuple(容器) set(容器)"""
print(f'列表转元组的结果是：{tuple(my_list)}')
print(f'元组转元组的结果是：{tuple(my_tuple)}')
print(f'字符串转元组结果是：{tuple(my_str)}')
print(f'集合转元组的结果是：{tuple(my_set)}')
print(f'字典转元组的结果是：{tuple(my_dict)}')

print('\n')

#类型转换：容器转字符串
"""语法：list(容器) str(容器) tuple(容器) set(容器)"""
print(f'列表转字符串的结果是：{str(my_list)}')
print(f'元组转字符串的结果是：{str(my_tuple)}')
print(f'字符串转字符串结果是：{str(my_str)}')
print(f'集合转字符串的结果是：{str(my_set)}')
print(f'字典转字符串的结果是：{str(my_dict)}')

print('\n')

#类型转换：容器转集合
"""语法：list(容器) str(容器) tuple(容器) set(容器)"""
print(f'列表转集合的结果是：{set(my_list)}')
print(f'元组转集合的结果是：{set(my_tuple)}')
print(f'字符串转集合结果是：{set(my_str)}')
print(f'集合转集合的结果是：{set(my_set)}')
print(f'字典转集合的结果是：{set(my_dict)}')

print('\n')

#sorted排序
"""语法：sorted(容器,[reverse=True])"""
my_list=[2,4,3,5,1]
my_tuple=(3,1,5,2,4)
my_str='南海十三郎江誉镠'
my_set={5,3,4,1,2}
my_dict={'key2':'程蝶衣','key4':'段小楼','key3':'柯南','key1':'灰原哀'}

print(f'列表对象的正向排序结果：{sorted(my_list)}')
print(f'元组对象的正向排序结果：{sorted(my_tuple)}')
print(f'字符串对象正向排序结果：{sorted(my_str)}')
print(f'集合对象的正向排序结果：{sorted(my_set)}')
print(f'字典对象的正向排序结果：{sorted(my_dict)}')

print(f'列表对象的反向排序结果：{sorted(my_list,reverse=True)}')
print(f'元组对象的反向排序结果：{sorted(my_tuple,reverse=True)}')
print(f'字符串对象反向排序结果：{sorted(my_str,reverse=True)}')
print(f'集合对象的反向排序结果：{sorted(my_set,reverse=True)}')
print(f'字典对象的反向排序结果：{sorted(my_dict,reverse=True)}')