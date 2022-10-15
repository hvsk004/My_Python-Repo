x=int(input("Enter a number : "))
if x<200:
    print("Variable is less than 200")
    if x<150:
        print("Variable is less than 150")
    elif x==150:
        print("Variable is 150")
    elif x<10:
        print("Variabke is less than 10")
else:
    print("Error 404")
print("Hello World")