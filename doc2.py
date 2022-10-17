def abc(a,b,c):
    if a>b and a>c:
        print(a,'is a greater')
    elif b>c and b>a:
        print(b,'is a greater')
    else:
        print(c,'is a greater')
a=int(input('enter the number'))
b=int(input('enter the number'))
c=int(input('enter the number'))
abc(a,b,c)