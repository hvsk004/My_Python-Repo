a=0
b=1
x=int(input("Enter the value of N: "))
print("0 1",end=' ')
for i in range(0,x-2):
    sum=a+b
    a=b
    b=sum
    i+=1
    print(sum,end=" ")
    
    

