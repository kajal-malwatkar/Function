# Your goal is to return multiplication table for number that is always an integer from 1 to
# 10.For example, a multiplication table (string) for number == 5 looks like below:- 1 * 5 =5
# 2 * 5 =10
# 3 * 5 =15
# .
# .
# 10 * 5=50
def num(a):
    i=1
    b=5
    while i<=a:
        print(i,'*',b,'=',i*b)
        i+=1
num(int(input('enter the numer')))