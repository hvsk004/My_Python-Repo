yearsOfservice=int(input("Enter the number of years of Service : "))

if yearsOfservice>=10:
   
    salary=int(input("Enter your Salary : "))
    
    netbonus=salary+(0.1*salary)
    
    print("Your Net Bonus is : ",netbonus)

elif yearsOfservice>=6 and yearsOfservice<10:
    
    salary=int(input("Enter your Salary : "))
    
    netbonus=salary+(0.08*salary)
    
    print("Your Net Bonus is : ",netbonus)

elif yearsOfservice>=0 and yearsOfservice<6:
   
    salary=int(input("Enter your Salary : "))
   
    netbonus=salary+(0.05*salary)
   
    print("Your Net Bonus is : ",netbonus)
else:
    print("Enter valid data")
