import math
print("Scientific Calculator Python Program")
c=int(input("Enter 1 For Addition\nEnter 2 For Subtraction\nEnter 3 For Multiplication\nEnter 4 For Division\nEnter 5 For Remainder(%)\nEnter 6 for Square Root\nEnter 7 for Exponent\nEnter 8 for Sine Function\nEnter 9 for Cosine function\nEnter 10 for Tnagent Function\nEnter 11 for Radians to degree conversion\nEnter 12 for Degree to Radina conversion\nEnter Your Choice: "))
def simplecalc(z):
    if z==1:
        x=float(input("Enter First Number : "))
        y=float(input("Enter Second Number : "))
        print("The sum is : ",x+y)
    elif z==2:
        x=float(input("Enter First Number : "))
        y=float(input("Enter Second Number : "))
        print("The answer is : ",x-y)
    elif z==3:
        x=float(input("Enter First Number : "))
        y=float(input("Enter Second Number : "))
        print("The Product is : ",x*y)
    elif z==4:
        x=float(input("Enter First Number : "))
        y=float(input("Enter Second Number : "))
        print("The answer is : ",x/y)
    elif z==5:
        x=float(input("Enter First Number : "))
        y=float(input("Enter Second Number : "))
        print("x%y")
    elif z==6:
        x=float(input("Enter the Number : "))
        
        print(math.sqrt(x))
    elif z==7:
        x=float(input("Enter the Number : "))
        
        print(x**y)
    elif z==8:
        x=float(input("Enter the Number : "))
        
        print(math.sin(x))
    elif z==9:
        x=float(input("Enter the Number : "))
        
        print(math.cos(x))
    elif z==10:
        x=float(input("Enter the Number : "))
        
        print(math.tan(x))
    elif z==11:
        x=float(input("Enter the Number : "))
        
        print(math.degrees(x))
    elif z==12:
        x=float(input("Enter the Number : "))
        
        print(math.radians(x))
    else:
        print("Enter Valid Inputs")
    
        
simplecalc(c)
