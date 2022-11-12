print("Simple Calculator Python Program")
c=int(input("Enter 1 For Addition\nEnter 2 For Subtraction\nEnter 3 For Multiplication\nEnter 4 For Division\nEnter Your Choice: "))
a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
def simplecalc(x,y,z):
    if z==1:
        print("The sum is : ",x+y)
    elif z==2:
        print("The answer is : ",x-y)
    elif z==3:
        print("The Product is : ",x*y)
    elif z==4:
        print("The answer is : ",x/y)
    else:
        print("Enter Valid Input")
simplecalc(a,b,c)
