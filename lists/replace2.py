numbers=[1,2,3,4,5,2,6]
flag=False
newList=[]
for x in numbers:
    if x!=2:
        newList.append(x)
    elif x==2 and flag==False:
        newList.append(x*100)
        flag=True
    elif x==2 and flag==True:
        newList.append(x)

print(newList)