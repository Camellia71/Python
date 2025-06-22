#定义元组字面量
"""
(元素，元素，...，元素)元素之间可以是不同的数据类型
"""
#定义元组变量
"""
变量名称=(元素，元素，...，元素)
"""
#定义空元组
"""
变量名=()       
变量名=tuple()
"""

t1=(1,'hellow',True)
print(f't1的类型是：{type(t1)}，t1的内容是：{t1}')

#定义一个元素的元组
t=('hellow',)
print(f't的内容是{t}')

#元组的嵌套
t5=((1,2,3),(4,5,6))
print(f't5的类型是：{type(t5)}，t1的内容是：{t5}')

#下标索引取出元素
print(t5[1][2])

#元组的操作：index查找
index=t1.index('hellow')
print(index)

#元组操作方法：count统计方法
t3=(2,3,5,8,7,4,6,9,5,3,0)
print(f't3中5出现了{t3.count(5)}次')

#元组操作方法：len
print(len(t3))

#元组的遍历
for element in t3:
    print(element,end=' ')

print('\n')

for i in range(len(t3)):
    print(t3[i],end=' ')