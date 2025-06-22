#演示使用构造方法对成员变量进行赋值
class Student:
    name=None
    age=None
    tel=None

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("Student类创建了一个类对象")

stu=Student("周杰伦",31,"120000089")
print(stu.name)
print(stu.age)
print(stu.tel)