str="Hello World"
print(str[:6])
print(str[8:])
for i in range(0,10):
    if str[i]==" ":
        x=i
        y=i+1
        print(str[:x])
        print(str[y:])
print(str.upper())
print(str.lower())
print(str.strip()) #It removes the spaces before the starting of the spring
print(str.replace("Hello", "Hi"))