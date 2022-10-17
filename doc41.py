# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def num(a):
    i=0
    c=0
    max=0
    while i<len(a):
        b=len(a[i])
        if max<b:
            c=a[i]
            max+=1
        i+=1
    print(max,c)
num([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])