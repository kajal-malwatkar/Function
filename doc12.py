# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

# def fun(a):
#     i=0
#     b=[]
#     while i<len(a):
#         c=str(a[i])
#         j=0
#         d=' '
#         while j<4:
#             # print(j)
#             if c[j]!=str(0):
#                 d=d+(c[j])
#                 g=int(d)
#             j+=1
#         b.append(g)
#         i+=1
#     print(b)
# fun([1450,1450,960000,1050])


def num(a):
    i=0
    b=[]
    while i<len(a):
        while a[i]>0 or a[i]<0:
            if a[i]%10!=0:
                b.append(a[i])
                break
            else:
                a[i]=a[i]//10
        i+=1
    print(b)
num([1450,9600,1050,-1050])

            
        
            
            
            