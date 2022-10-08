from math import sqrt
a=input("Enter the length of side A ")
b=input("Enter the Length of side B ")
c=input("Enter Tthe length of side C ")
s=(int(a)+int(b)+int(c))/2
A=sqrt(int(s)*(int(s)-int(a))*(int(s)-int(b))*(int(s)-int(c)))
print("The Area of the triangle is",A)