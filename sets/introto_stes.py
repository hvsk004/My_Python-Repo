#Store multiple Values in single variable
#Unordered
#unchangable or unmutable
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