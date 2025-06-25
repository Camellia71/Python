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

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621201855437.png" alt="image-20250621201855437" style="zoom:80%;" />

![image-20250621202000795](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250621202000795.png)

```python
#range函数
range (start,end,step)
#start:起始，可以省略
#end:结束的数字，但不包含在内
#step：两个数的间隔，默认为1，可以省略
```

**重点**

break是跳出最内层的for或者while循环，而后执行下一步；continue只结束本次循环，然后进行下一次循环；

## 3.序列

![image-20250622003706471](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622003706471.png)

> [!NOTE]
>
> 索引有两种表示方法：
>
> 一种是从左往右，即从0到n-1
>
> 另一种是从右往左，即从-1到-n

序列操作符

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622004022117.png" alt="image-20250622004022117" style="zoom:80%;" />

##### 1.列表

列表是包含0个或多个元素的有序序列，属于序列类型

可以进行增删改查等操作，没有长度显示，元素类型可以不同

列表可以用[ ]表示，也可以用list() 函数将字符串或者集合转化成列表，list函数可以生成空列表

列表的索引：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622171808997.png" alt="image-20250622171808997" style="zoom:50%;" />

列表的切片：切片之后还是列表

```python
ls = [1010,"1010",[1010,"1010"],1010]
print(ls[0:4:2])
```

列表的函数：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622173253395.png" alt="image-20250622173253395" style="zoom:50%;" />

列表操作：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622182634620.png" alt="image-20250622182634620" style="zoom:50%;" />

##### 2.元组

元组是python中的一个序列，与列表类似，但是他是不可变序列

```python
t = (1,2,3)
type(t)
#<class 'tuple'>
#另一种方法
t = tuple(range(1,2,3))
```

元组的操作

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622184213159.png" alt="image-20250622184213159" style="zoom:50%;" />

##### 3.字典

字典是通过键值对的方式来呈现的，就是一一对应，这种也可以叫做映射；

```python
d = {"112211":"张岐奕","112222":"camellia","112233":"71",112211:"qiyi"}
print(d)
print(d[112211])
d["112211"]="新张岐奕"
print(d["112211"])
```

字典的操作函数：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622195552869.png" alt="image-20250622195552869" style="zoom:50%;" />

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622195637157.png" alt="image-20250622195637157" style="zoom:67%;" />

字典的操作方法：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622195712599.png" alt="image-20250622195712599" style="zoom:50%;" />

##### 4.集合

集合内的元素不可重复，元素类型也只能是不可变类型；列表，集合都是可变数据类型，不能作为集合的元素出现

转化为集合类型可以筛掉重复的元素

操作符：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622200528819.png" alt="image-20250622200528819" style="zoom: 50%;" />

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622200655901.png" alt="image-20250622200655901" style="zoom:50%;" />

集合操作方法：

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622200757866.png" alt="image-20250622200757866" style="zoom: 50%;" />

## 4.字符串

![image-20250622201403547](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622201403547.png)

##### 1.操作符

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622201919428.png" alt="image-20250622201919428" style="zoom:50%;" />

##### 2.处理函数

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622202037025.png" alt="image-20250622202037025" style="zoom: 50%;" />

##### 3.处理方法

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622202238072.png" alt="image-20250622202238072" style="zoom:67%;" />

##### 4.编码转换

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622204112053.png" alt="image-20250622204112053" style="zoom:67%;" />

![image-20250622204227956](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622204227956.png)

##### 5.占位符和format

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622204408757.png" alt="image-20250622204408757" style="zoom:67%;" />

![image-20250622204534860](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622204534860.png)

format：

```python
"{0} {1} {1} {0}".format("li hua,24")
#'li hua 24 24 li hua'
```

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622204954336.png" alt="image-20250622204954336" style="zoom:67%;" />

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622205034753.png" alt="image-20250622205034753" style="zoom:67%;" />

<img src="C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20250622205908637.png" alt="image-20250622205908637" style="zoom:67%;" />

## 5.函数

##### 1.函数的定义与调用

```python
def hanshu(xingcan):
	daima
	return fanhuizhi
```

```python
def n(i):
    s = 1
	for i in range(1,i):
	s*=i
	return s
```

##### 2.函数的传递参数

```python
def n(x,y = 10):
	return(x * y)
print(n(10))
#100
print(n(10,2))
#20
```

##### 3.全局变量和局部变量

如果要在函数内部使用全局变量，则要在函数内加global

```python
n = 2
def tn(x,y):
	global n
	return n * x * y
print(tn(2,3))
```

##### 4.临时函数

lambda函数，又被称为匿名函数，代表临时使用的简单函数

```python
f = lambda x,y,z:x+y+z
f(10,20,30)
#60
```

