def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(n-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

b=[1,5,6,4,7,8,9,3,0,2]
a=bubble_sort(b)
print(*a)
