
#  aver=sum/3.0

#  str1='SDUTCSSEno1'
#  str1[-6:-1]
#  print(chr(65))
#  x=3.1415926
#  print(round(x,2) ,round(x))

#  x=eval()
#  y=eval()
#  z=eval()
#  s=x+y+z
#  avg=s/3
#  print("和:",s)
#  print("平均:",f"{avg:.4f}")
#  x=str(input())
#  print("地区编号：",x[1:6])
#  print("出生日期：",x[-12:-5])
# print("hello world")
# pip install numpy pandas scikit-learn matplotlib

# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# import matplotlib.pyplot as plt

# print("所有库导入成功！")

# temp = 1
# if not(temp > 10):
#     print("太冷了！")
# else:
#     print("明天见！")
# temp = 1
# if temp > 10:
#     print("太冷了！")
# print("明天见！")

# temp = 1
# if not(temp > 10):
#     print("太冷了！")
# else:
#     print("明天见！")
# temp = 1
# if temp < 10:
#     print("太冷了！")
# else:
#     print("明天见！")
# temp = 1
# if temp > 10:
#     print("太冷了！")
#     print("明天见！")
# temp = 1
# if temp > 10:
#     print("太冷了！")
# print("明天见！")
# s=0
# # a,b=1,2
# # if a>0:
# #     s=s+1
# # elif b>0:
# #     s=s+1
# # print(s)
# def Foo(x):
#  if (x==1):
#   return 1
#  else:
#   return x+Foo(x-1)
# print(Foo(4))

# print("输出结果是{:3.2f}".format(12.345))
# def foo(x1,x2=3,x3=5):
#     foo(2,7)

# x = 0
# while x<10:
#     if x%2 == 1:
#         continue
#     x = x + 1
#     print(x)
# def median(aList):
#     # number = list(aList)
#     # number = [int(x) for x in aList]
#     number = []
#     for x in aList:
#         number.append(int(x))
#     number.sort()
#     n = len(number) 
#     if n % 2 != 0:
#         return number[n//2]
#     else:
#         mid1 = number[(n // 2)- 1]
#         mid2 = number[n // 2]
#         return (mid1+mid2)/2

# def main():
#     age = list(input().split())
#     print(median(age))
        
# main()
# def prime(num):
#     if num < 2:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#     return True
# n =  int(input())
# for i in range(n-1,1,-1):
#     if prime(i):
#         print(i)
#         break
# n = int(input())
# longest = input()
# for i in range(1,n-1):
#     s = input()
#     if len(s) > len(longest):
#         longest = s
# longest = "111"
# print(f"最长的是:{longest}")
n = int(input())
print(n)