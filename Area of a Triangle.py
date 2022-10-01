from math import sqrt
from re import A
a=input("Enter the length of 1st side ")
b=input("Enter the length of 2nd side ")
c=input("Enter the length of 3rd side ")
s=(int(a)+int(b)+int(c))/2
x=int(s)-int(a)
y=int(s)-int(b)
z=int(s)-int(c)
A=int(s)*int(x)*int(y)*int(z)
print("The area of the Triangle is",sqrt(int(A)))