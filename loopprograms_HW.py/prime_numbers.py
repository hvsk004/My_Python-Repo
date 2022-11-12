a=int(input("Enter the Starting Number of the Range :"))
b=int(input("Enter the Ending Number of the Range :"))
if a>1:
   for i in range(a,b+1):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
            break
    if flag==False:
        print(i)

    