import time
#运行前时间
t1=time.time()
a=0

#中间程序运算过程
for i in range(10):
    a+=i
print(a)

#运行后时间
t2=time.time()
print(t2-t1)