## 1.基础语法

##### 1.注释

单行注释用#；多行注释用‘’‘ 或“”“ 

```python
print("hello.world!")  #单行注释
'''
多行注释
'''
```

![image-20250620184309494](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250620184309494.png)

##### 2.续行符

​	\

```python
print(\
	"hello"\
	"world"\
)
#结果是 hello world
```

##### 3.保留字

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621111231913.png" alt="image-20250621111231913" style="zoom:80%;" />

##### 4.变量

```python
n = 10  #把10赋值给n
n = 95
n = 100
#变量一旦有了新的值，之前的值就被覆盖了，也就是说，变量只能容纳一个值；
```

```python
name,age = 'Lucy',18  #同时赋给多个变量
```

##### 5.基本数据类型

![image-20250621112000597](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621112000597.png)

![image-20250621112156708](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621112156708.png)

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621112256121.png" alt="image-20250621112256121" style="zoom:67%;" />

字符串下标：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621112449271.png" alt="image-20250621112449271" style="zoom:67%;" />



数据类型转换

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621112704348.png" alt="image-20250621112704348" style="zoom:80%;" />

##### 6. 运算符

![image-20250621112944932](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621112944932.png)

位运算符：

![image-20250621113350386](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621113350386.png)

身份运算符：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621113426169.png" alt="image-20250621113426169" style="zoom:80%;" />

id( )函数用于获取对象的内存地址

成员运算符：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621113526589.png" alt="image-20250621113526589" style="zoom:80%;" />

运算符优先级：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621113617978.png" alt="image-20250621113617978" style="zoom:80%;" />

##### 7.输入输出语句

input

```python
str = input()
#input函数接收键盘输入，返回字符串类型
```

eval

```python
r = eval(input("请输入有效表达式："))
#计算字符串所对应的表达式的值，返回计算结果
```

print

```python
print("hello,world")
print(10)
```

## 2.流程控制语句

顺序结构，分支结构（if），循环结构（for，while）

```python
name = input("请输入姓名：")
print("姓名是：",name)
```

```python
r = input("请输入数字：")
r = int(r)
if r > 5 and r < 10:
    print(1)
elif r > 3:
    print(2)
else:
    print(3)
```

```python
count = 0
while count < 5 :
	print("小于5")
	if count == 2:
		break
	count += 1
else:
	print("等于2了")
#else是while循环内部的，break跳出循环
```

例题：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621185219827.png" alt="image-20250621185219827" style="zoom:80%;" />

```python
#for 循环语句 in 遍历结构
	#语句块

```

