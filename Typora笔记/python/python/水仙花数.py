for i in range(100,1000):
    a=i//100
    b=i%100//10
    c=i%100%10
    if i==a**3+b**3+c**3:
       print(i,end=' ')

