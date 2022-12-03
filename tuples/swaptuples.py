tuple1=(10,20)
tuple2=(30,40)
temp=tuple1
tuple1=tuple2
tuple2=temp
print("tuple1 = ",tuple1)

print("tuple2 = ",tuple2)
#Second Method
tuple3=(12,24)
tuple4=(16,32)
tuple3,tuple4=tuple4,tuple3
print(tuple3)
print(tuple4)