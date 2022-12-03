a=0
b=1
a=[]
while True:
    x=input("Input :")
    if x=='':
        break
    else:
        b=int(x)
    a.append(x)
a.sort()
p=len(a)
z=int(a[-1])
fib=[0,1]
a=0
b=1
x=z
fib=[0,1]
for i in range(0,x+1):
    sum=a+b
    a=b
    b=sum
    fib.append(sum)


for i in range(p):
    
    if a[i] in fib:
        
         print(True)
    

