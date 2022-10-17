# Write a function to check if a number is even or not.

def even(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]%2==0:
            b.append(a)
        i+=1
    print(b,'even number')
even([12])