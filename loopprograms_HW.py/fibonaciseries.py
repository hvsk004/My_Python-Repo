a=0
b=1
print("0 1",end=' ')
for i in range(0,12):
    sum=a+b
    a=b
    b=sum
    i+=1
    print(sum,end=" ")
    
    

