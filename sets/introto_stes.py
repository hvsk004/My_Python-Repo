#Store multiple Values in single variable
#Unordered
#unchangable or unmutable but we can add and remove elements
#Duplicates are not allowed
myset={'Supercar','Superbike','Yacht'}
print(myset)
myset2={'car','bike','car','boat'}
print(myset2)
print(len(myset))
a='superbike'
print(a in myset2)
for i in myset2:
    if a==i:
        print(True)
    else:
        print(False)
myset3=myset.union(myset2)
print(myset3)