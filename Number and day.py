from cgi import print_form


number=int(input("Enter any number between 1 to 7 to get the day : "))
if number==1:
    print("Sunday")
elif number==2:
     print("Monday")
elif number==3:
    print("Tuesday")
elif number==4:
    print("Wednesday")
elif number==5:
    print("Thursday")
elif number==6:
    print("Firday")
elif number==7:
    print("Saturday")
else:
    print("Enter a valid number")
