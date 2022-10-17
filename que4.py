
# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()

# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")

# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

# def info(name, age ="17"):
#     print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","kajal")

# def isGreaterThan20(a, b = 20):
#     if a > 20 and b > 20:
#         print('True')
#     elif a <= 20 or b <= 20:
#         print('False')
# isGreaterThan20(20)

# def add(number1,number2):
#     print(number1+number2)
# #calling function with two arguments as function is defined with two parameters
# add(12,56)

# def check_numbers(a,b):
#     for i in range(len(a)):
#         if(a[i]%2==0 and b[i]%2==0):
#             print("both are even")
#         else:
#             print("both numbers are not even")
# l1=[10,13,20,21,22]
# l2=[16,18,19,21,27]
# check_numbers(l1,l2)

# def fun(l1,l2):
#     for i in range(len(l1)):
#         sum=l1[i]+l2[i]
#         print(sum)
# #passing two list as an arguments to our function
# list1=[10,20,30]
# list2=[40,50,60]
# fun(list1,list2)

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"
# print("Will I be able to print? :-(")

# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# print(fri_menu)

# def calculator(number_x,number_y,operation):
#     l=[]
#     if(operation=="add"):
#         print(number_x+number_y)
#     elif(operation=="sub"):
#         print(number_x-number_y)
#     elif(operation=="divide"):
#         print(number_x/number_y)
#     elif(operation=="multiply"):
#         for i in range(len(number_x)):
#             mul=number_x[i]*number_y[i]
#             l.append(mul)
#             print(l)
#     else:print("invalid request")
# l1=[10,20,30,40]
# l2=[50,60,70,80]
# calculator(l1,l2,"multiply")

# def distance(kms):
#     if kms <= 20:
#         print("close")
#     elif kms < 50:
#         print("median")
#     else:
#         print(far)
# distance(20)


# def abc(a,b,c):
#     if a>b and a>c:
#         print(a,'is a greater')
#     elif b>c and b>a:
#         print(b,'is a greater')
#     else:
#         print(c,'is a greater')
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# abc(a,b,c)




# Your task is to create function is Divided By (or is_divide_by) to check if an integer
# number is divisible by each out of two arguments.
# A few cases:
# (-12, 2, -6) -> true

# side1=int(input('enter the angle'))
# side2=int(input('enter the angle'))
# side3=int(input('enter the angle'))
# if side1==side2==side3==180:
#     print('triangle is equilateral')
# elif side1==side2+side3==180 or side2==side3+side1==180 or side3==side1+side2==180:
#     print('triangle is isosceles')
# elif side1+side2+side3==180:
#     print('triangle is scalene')
# else:
#     print('the given angles is not equal to 180 degree. Try again')    


# a=input('enter the letter')
# if 'a' in a or 'e' in a or 'i' in a or 'o' in a or 'u' in a:
#     print('vowels')
# else:
#     print('consonants')

# a=[1,2,3,4,5,6]
# b=[2,3,1,0,6,7]
# i=0
# c=[]
# while i<len(a):
#     if a[i] not in b:
#             c.append(a[i])
#     i=i+1
# print(c)

# ch=input('enter the letter')
# if ch>='A' and ch<='Z':
#     print('uppercase')
# elif ch>='a' and ch<='z':
#     print('lowercase')
# else:
#     print("try again, it's not a alphabet letter")
    

# print("dfghj")
# a=3
# def A():
#     print("hi")
#     b=5
#     c=a+b
#     return c
# print(A())
# print("jyo")
# b=8

# a=[3,5,6,8,-1]
# i=0
# min=0
# while i<len(a):
#     if a[i]<min:
#         min=a[i]
#     i=i+1
# print(min)

# num=[50,40,23,70,56,12,5,10,7]
# count=0
# i=1
# while i<len(num):
#     if num[i]>=20 and num[i]<=40:
#         count=count+1
#     i=i+1
# print('number of elements in the list',count)



# def num(n):
#     if n % 2 ==0:
#         print('Even')
#     else:
#         print('Odd')
# num(int(input('enter the number')))

# a=[1,2,3,[6,7],8]
# b=[]
# i=0
# while i<len(a):
#     j=2
#     while j<len(a):
#         a[i]*[j]
#         j=j+1
#     i=i+1
# print(a[i*j])

# print("Enter the Number of Days: ")
# num = int(input())

# year = int(num/365)
# week = int((num%365)/7)
# days = int((num%365)%7)

# print("Total Number of Year(s): ")
# print(year)
# print("Total Number of Week(s):")
# print(week)
# print("Total Number of Day(s):")
# print(days)


# date=int(input("enter the date"))
# month=int(input("enter the month"))
# year=int(input("enter the year"))
# if (date>0 and date<31):
#     date+=1
#     print(year,"/",month,"/",date)
# elif (date==31 or month==12):
#     print(year+1,1,1)
# else:
#     print("not next day")

# from re import I

# a=int(input('enter the number'))
# if a<=10:
#     print(a,'*',1,'=',a*1)
#     print(a,"*",2,'=',a*2)
#     print(a,"*",3,'=',a*3)
#     print(a,"*",4,'=',a*4)
#     print(a,"*",5,'=',a*5)
#     print(a,"*",6,'=',a*6)
#     print(a,"*",7,'=',a*7)
#     print(a,"*",8,'=',a*8)
#     print(a,"*",9,'=',a*9)
#     print(a,"*",10,'=',a*10)

    