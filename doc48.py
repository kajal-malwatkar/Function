# a='Tanujakhose'
# e=a[0:4:1]
# b='2.5'
# f=15+2j
# u=float(b)
# k=int(u)
# c=k+f
# y=str(c)
# print(a[0:4]+a[4:6].capitalize()+a[6:11].capitalize()+y)


# Two numbers are entered through the keyboard. Write a flowchart to find the value of the first number
# raised to the power of another.
# Sample Input
# 3
# 4
# Sample Output
# 81 (3x3x3x3)

def num(n):
    b=int(input('Enter the power'))
    c=n**b
    print(c)
num(int(input('enter the num')))