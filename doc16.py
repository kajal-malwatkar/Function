# Print multiplication table of 12 using function
def table(a):
    i=0
    while i<10:
        i+=1
        print(a,'*',i,'=',a*i)
table(int(input('enter the number')))