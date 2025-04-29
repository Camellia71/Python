# def mysum(x):
#     s=0
#     x=abs(x)
#     while x>0:
#         s+=x%10
#         x//=10
#         return s
# def mysum(x):
#     sum_digits=0
#     if x<0:
#         x=-x
#     while x :
#         sum_digits+=x%10
#         x=x//10
#         return sum_digits

# 
# def average(*x):
#     if not x:
#         return 0
#     return sum(x)/len(x)

# x1,x2,x3,x4=map(eval,input().split())
# b=average(x1,x2)
# print('两个数平均值为：{:.2f}'.format(b))
# b=average(x1,x2,x3)
# print('三个数平均值为:{:.2f}'.format(b))
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)

# n = int(input())
# print(fact(n))

# num = input()
# num_str=str(abs(int(num)))
# digit_count={str(i):0 for i in range(10)}
# for char in num_str:
#     if char.isdigit():
#         digit_count[char] +=1
# for i in range(10):
#     print(f"{i}:{digit_count[str(i)]}")

# s1="Life is short . I use Python."
# s2=input()
# s1_lower=s1.lower()
# s2_lower=s2.lower()
# if s2_lower in s1_lower:
#     print('Yes')
# else:
#     print("No")

s=input()
letter_count=0
digit_count=0
other_count=0
for char in s:
    if 'a' <= char.lower() <= 'z':
        letter_count +=1
    elif '0' <= char <= '9':
        digit_count +=1
    else:
        other_count +=1
print(f"英文字母{letter_count}个，数字字符{digit_count}个，其他字符{other_count}个")
