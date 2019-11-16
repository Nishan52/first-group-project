import sys
import math
name=input("Please enter your name")
while name.isalpha()==False or len(name)<4 :
    if ' ' in name :
        break
    else:
        print("THE NAME YOU ENTERED IS INCORRECT")
    name=input('Enter name again')
print("WELCOME! NOW YOU ARE READY TO USE CALCULATOR \n YOU HAVE FOLLOWING OPTIONS")
doagain='yes'
while doagain=='yes':
    print("Select operation")
    print("1.Add           2.Subtract")
    print("3.Multiply      4.Modulous")
    print("5.square root   6. Square")
    print("7.division")
    select=int(input("your choice operation 1/2/3/4/5/6/7     "))
    if select==1:
        num1=int(input("Enter your number"))
        addagain='yes'
        while addagain=='yes':
            num2=int(input("Enter your number again"))
            result=num1+num2
            addagain=input("do you want to add more number")
        print("The sum of the given number is ",result)
    elif select==2:
        a=int(input("Enter your first number"))
        subtractagain='yes'
        a=0
        b=0
        while subtractagain=='yes':
            b=int(input("Enter the number you want to subtract"))
            c=a-b
            subtractagain=input('Do you want to subtract more number')
        print("The resulrt is",c)
    elif select==3:
        num1 = int(input("Enter the first number"))
        mulagain='yes'
        while mulagain=='yes':
            num2=int(input("Enter your number "))
            product=num1*num2
            mulagain=input("do you want to multiply more number")
        print("the product of the given number is",product)
    elif select==4:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        rem=num1%num2
        print("The remainder of the given division number is",rem)
    elif select==5:
        num1 = int(input("Enter the number"))
        sqroot=math.sqrt(num1)
        print("The square root of the given number is ",sqroot)
    elif select==6:
        num1 = int(input("Enter the number"))
        square=num1*num1
        square=int(square)
        print("The square of the given number is ",square)
    elif select==7:
        num1 = int(input("Enter the first number"))
        num2 = int(input("Enter the second number"))
        quoitent=num1/num2
        print("The Quoitent of the given number is",float(quoitent))
    else:
        sys.exit("OPERATION OUT OF THE RANGE")
    doagain=input("\nYou want to do other calculation:(yes/no)     ")
