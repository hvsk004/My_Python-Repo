a=int(input("Enter the length of First Side : "))
b=int(input("Enter the length of Second Side : "))
c=int(input("Enter the lenght of Third Side : "))
s=int((a+b+c)/2)
Area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of the Triangle is :",Area)