# Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def code(a):
    i=0
    b=[]
    c=[]
    while i<len(a):
        if a[i]>='A' and a[i]<='Z':
            b.append(a)
        elif a[i]>='a' and a[i]<='z':
            c.append(a)
        i+=1
    print('No. of Uppercase :',len(b))
    print('No. of Lowercase :',len(c))

code('The quick Brow Fox')