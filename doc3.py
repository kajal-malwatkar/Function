# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20

def list(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i+=1
    print(sum)
list((8,2,3,0,7))
