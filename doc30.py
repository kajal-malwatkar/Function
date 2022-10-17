# Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter
def num(n):
    c=0
    i=1
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if c==2:
        print('prime numbers')
    else:
        print('not prime number')
num(n=int(input('enter the number :')))