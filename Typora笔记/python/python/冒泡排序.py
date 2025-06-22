a=[1,5,6,8,9,7,4,3,2,0]
for i in range(10):
    for j in range(10-1-i):
        if a[j]>a[j+1]:
            """ t=a[j]
                a[j]=a[j+1]
                a[j+1]=t"""
            a[j],a[j+i]=a[j+i],a[j]
#print(a)
print(*a)