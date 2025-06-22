#语法：lambda 传入参数：函数体(一行代码)
"""
1.lambda是关键字，表示定义匿名函数
2.传入参数表示匿名函数的形式参数，如：x,y表示接收2个形式参数
3.函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
"""

#常规方法
def test_func(compute):
    result=compute(1,2)
    print(result)

def compute(x,y):
    return x+y

test_func(compute)

#lambda函数方法
def test_func(compute1):
    result=compute1(1,2)
    print(result)

test_func(lambda x,y:x+y)