#Ordered
#Changable
#Does not allow duplicate values
dict1={
    "name":"Krishna",
    "age":18,
    "age":"18",
    "CGPA":8.9
}
print(dict1)
dict2=dict1.copy()
print(dict1.get("CGPA"))
print(dict1.keys())
print(dict1.values())
dict1["Reg no"]=12219635
print(dict1.items())
dict1["age"]=19
print(dict1.items())
dict1.update({"CGPA":9.0})
print(dict1)                    
dict1.pop("Reg no")
print(dict1)
dict1.popitem()
print(dict1)
print(dict2)