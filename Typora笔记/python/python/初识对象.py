#1.设计一个类
class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None

#2.创建一个对象
stu_1 = Student()

#3.对象属性进行赋值
stu_1.name='鱼嘉诚'
stu_1.gender='男'
stu_1.nationality='中国'
stu_1.native_place='陕西省'
stu_1.age=18

#4.获取对象中记录信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)