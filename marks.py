marks=int(input("Enter your Marks : "))
if marks>90 and marks<=100:
    print("Your grade is A")
elif marks>80 and marks<=90:
    print("Your grade is B")
elif marks>70 and marks<=80:
    print("Your grade is C")
elif marks>60 and marks<=70:
    print("Your grade is D")
elif marks>50 and marks<=60:
    print("Your grade is E")
elif marks<50:
    print("Your grade is F")
else:
    ("Enter A valid number")