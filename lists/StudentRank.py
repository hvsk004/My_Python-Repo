from operator import __add__
Names=["Ramesh","Suresh","Dinesh","Ganesh","Kuresh","Paramesh","Sandesh","Mukesh"]
Marks=[40,45,25,56,38,43,54,32]
Changeinmarks=[12,6,44,2,12,3,8,9,10]
def zipandsort(list1,list2):
    zip_pair=zip(list1,list2)
    z=[x for _,x in sorted(zip_pair)]
    return z
oldar=zipandsort(Marks,Names)
finalMarks=list(map(__add__,Marks,Changeinmarks))
newar=zipandsort(finalMarks,Names)
oldar.sort(reverse=True)
newar.sort(reverse=True)
a=newar[-1]
change_in_rank=oldar.index(newar[-1])
print("The Student with the Highest Marks is",a,"and the change in rank is",change_in_rank)