# Create a function that takes 2 positive integers in form of a string as an input, and outputs the
# sum (also as a string):
# "4", "5" --> "9"
# "34", "5" --> "39"
# Notes:
# If either input is an empty string, consider it as zero.

def s(num1):
    i=0
    b=[]
    while i<len(num1):
        g=str(num1[i])
        j=0
        sum=0
        while j<len(g):
            sum=(sum)+int(g[j])
            j+=1
        i+=1
        print(sum)
s(['34'])
