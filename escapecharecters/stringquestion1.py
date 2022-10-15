from math import ceil, floor
str=str(input("enter a string : "))
z=int(len(str))
a=float((z-1)/2)
b=int(floor(a))
c=int(ceil(a))
print("The first charecter is : ",str[0])
if (z-1)%2==0:
    print("The middle charecter is : ",str[c])
else:
    print("The middle charecters are  ",str[b],str[c])
print("The last charecter is :  ",str[z-1])