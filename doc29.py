# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit
# (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18,
# 20.

def num(a):
    i=0
    sum=0
    while i<len(a):
        if a[i]%3==0 or a[i]%5==0:
            sum=sum+a[i]
        i+=1
    print(sum)
num([3,5,6,9,10,12,15,18,20])