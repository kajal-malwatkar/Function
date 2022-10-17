# Make a function that receive age, and return what they drink.

def age(n):
    if n<=14:
        print('kids drink toddy.')
    elif n>=15 and n<=18:
        print('Teens drink  coke.')
    elif n>=19 and n<=21:
        print('Young adults drink beer.')
    else:
        print('Adults drink whisky.')
age(int(input("enter the age : ")))
        