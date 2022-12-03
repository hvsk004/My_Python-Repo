tuple1=(1,[6,7],2,3,4,5)
list1=list(tuple1)
list1[1][0]=8
tuple1=tuple(list1)
print(tuple1)