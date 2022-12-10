list1=['a','B','C','D','e','f']
print(list1)
print(list(map(lambda i:i.swapcase(),list1)))
for i in list1:
    if str(i).isupper()==True:
        i.lower()
    else:
        i.lower()
print(list1)