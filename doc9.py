# Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def list():
    i=1
    b=[]
    c=[]
    while i<=30:
        if i<=5:
            a=i**2
            b.append(a)
        elif i>=25:
            d=i**2
            c.append(d)
        i+=1
    print(b,c)
list()