def list(a):
    i=0
    c=0
    while i<len(a):
        b=a[i]
        if b[0]==b[-1]:
            c+=1
        i+=1
    print(c)
list(['abc', 'xyz', 'aba', '1221'])