'''
a=int(input("Enter your number"))
subtractagain='yes'
a=0
b=0
while subtractagain=='yes':
    b=int(input("Enter your number"))
    c=a-b
    subtractagain=input("want to subtract more num from initial num")
print("result",c)
'''
a=int(input("Enter your first number "))
mulagain='yes'
while mulagain=='yes':
    b=int(input("Enter your number again "))
    c=a*b
    mulagain=input("do you want to multiply more number")
print("The product of the entered number is ",c)
