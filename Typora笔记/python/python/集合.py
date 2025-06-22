#定义集合
my_set={"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_set_empty=set('誉镠')
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")
print(f"my_set的内容是：{my_set_empty},类型是：{type(my_set_empty)}")

#添加新元素
"""语法：集合.add(元素)"""
my_set.add('誉镠')
print(my_set)

#移除元素
"""语法：集合.remove(元素)"""
my_set.remove("黑马程序员")
print(my_set)

#随机取出一个元素
"""集合.pop(元素)"""
print(my_set.pop())

#清空集合
"""集合本身被清空"""
"""语法.clear()"""
my_set_empty .clear()
print(my_set_empty)

#取2个集合的差集（取出集合1和集合2的差集=集合1有而集合2没有的）
"""集合1.difference(集合2)"""
set1=my_set .difference(my_set_empty )
print(set1)

#消除2个集合的差集(在集合1中消除和集合2相同的元素)
"""集合1.difference_update(集合2)"""
set1=my_set .difference_update(my_set_empty )
print(my_set)

#2个集合合并为1个
"""语法:集合1.union(集合2)"""
set2={1,2,3}
set3={1,5,6}
set4=set2.union(set3)
print(set4)

#统计集合元素数量len()
print(len(set4))

#集合遍历
my_set={"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
for element in my_set:
    print(element)
