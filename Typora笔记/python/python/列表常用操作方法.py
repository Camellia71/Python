a=[1,2,5,4,6,8,9,7,3,0]

#1.查找某元素在列表中的下标
"""列表.index(元素)"""
n=input('要查找的元素：')
a_index=a.index(int(n))
print(a_index)

#2.修改特定下标索引值
"""列表[下标]=元素"""
a[3]=520
print(*a)

#3.在指定下标位置插入单个新元素
"""列表.insert(插入后的位置，'元素')"""
a.insert(1,'666')
print(*a)

#4.在列表的尾部插入新元素
a.append(606)
print(*a)

#5.在列表尾部插入一批新元素
"""列表.extend(其他数据容器)"""
b=[111,222,333]
a.extend(b)
print(*a)

#6.删除指定下标的元素（2种方法）
"""
1.del 列表[下标]
2.列表.pop(下标)
"""
del a[4]
print(*a)
a.pop(1)
print(*a)

#7.删除某元素在列表中的第一个匹配项
"""列表.remove(元素)"""
a.remove(333)
print(*a)

#8.清空列表
"""列表.clear()"""
a.clear()
print(a)

#9.统计列表内‘指定元素’数量
"""列表.count(元素)"""
a=[1,2,5,4,6,8,9,7,3,0,5,8]
count=a.count(5)
print(count)

#10.统计列表内所有元素数量
"""len(列表)"""
length=len(a)
print(length)

#11.列表的遍历
index=0
while index<len(a) :
    print(a[index],end=' ')
    index+=1

print('\n')

for i in range(len(a)):
    print(a[i],end=' ')