def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return  fibonacci(n - 1) + fibonacci(n - 2)

#num=0
#n=input('请输入要计算的斐波那契数列的项数：')
for i in range(1,11):
    print(fibonacci(i))

#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    return fibonacci(n - 1) + fibonacci(n - 2)
#
## 测试，例如求前10项
#for i in range(10):
#    print(fibonacci(i))#