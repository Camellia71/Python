my_str=' it yujiacheng and itcase '
#下标索引取值(正反向下标)
print(my_str[15])
print(my_str[-5])

#index方法
print(my_str.index('yu'))

#replace方法(将字符串内的全部字符串1替换为字符串2)
"""字符串.replace(字符串1，字符串2)"""
new_str=my_str.replace('and','&')
print(new_str)

#split方法
"""字符串.split(分隔符字符串)"""
print(my_str.split(' '))

#strip方法(规整)
"""语法：字符串.strip(参数)"""
print(my_str.strip())

#count统计字符串中字符出现的次数
print(my_str.count("i"))

#统计字符串长度
print(len(my_str))