a=[2,7,9,8,6,4,3,5,1,0]
for i in range(10):
    for j in range(10):

        if a[i]>a[j]:
           a[i],a[j]=a[j],a[i]
print(*a)

