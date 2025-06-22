class Student:
#__init__: 创造方法   
    def __init__(self,name,age):
        self.name=name
        self.age=age

#__str__:字符串方法
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

#__lt__:<、>符号比较
    def __lt__(self,other):
        return self.age<other.age    

#__le__:≤、≥符号比较
    def __le__(self,other):
        return self.age<=other.age  

#__eq__:==符号比较
    def __eq__(self,other):
        return self.age==other.age  

stu =Student("周杰伦",31)
print(stu)
print(str(stu))

stu1=Student("周杰伦",31)
stu2=Student("林俊杰",36)
stu3=Student("周华健",35)
print(stu2>stu3)
print(stu1>=stu3)
print(stu1==stu2)        




