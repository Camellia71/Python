#字符串格式化方式1
name='鱼嘉诚'
age=18
address='西安市'
information='个人信息：姓名：%s 年龄：%d 地址：%s' % (name,age,address)
print(information)

#字符串格式化方式2
name='鱼嘉诚'
age=18
address='西安市'
information=f'个人信息：姓名：{name} 年龄：{age} 地址：{address}'
print(information)