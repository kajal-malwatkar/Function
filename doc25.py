# Given a list of numbers, write a Python program to count positive and negative numbers in a List using
# function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
def list(a):
    b=[]
    i=0
    c=[]
    while i<len(a):
        if a[i]<0:
            b.append(a)
        else:
            c.append(a)
        i+=1
    print('Negative numbers',len(b))
    print('Positive numbers',len(c))
list([2,-7,5,-64,14])
    