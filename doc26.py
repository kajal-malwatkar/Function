# Write a function called fizz_buzz that takes a number.
# 1. If the number is divisible by 3, it should return “Fizz”.
# 2. If it is divisible by 5, it should return “Buzz”.
# 3. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# 4. Otherwise, it should return the same number.

def fun(a):
    if a%3==0:
        print('Fizz')
    if a%5==0:
        print('Buzz')
    if a%3==0 or a%5==0:
        print('Fizz Buzz')
    else:
        print('return',a)
fun(int(input('enter the number')))
    