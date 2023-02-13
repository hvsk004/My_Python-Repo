class Vehicle:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
class Bus(Vehicle):
    pass
bus=Bus("bus",12)
print(bus.name,bus.mileage)



# # print(len("Hello"))
# # print(len([10,20,30]))

# # def add(x,y,z = 0):
# #     return x+y+z

# # print(add(3,4))
# # print(add(3,4,5))



# # class India:
# #     def capital(self):
# #         print("New Delhi")
    
# #     def language(self):
# #         print("Hindi")
# #     def type(self):
# #         print("Developing")

# # class USA:
# #     def capital(self):
# #         print("Washington DC")
    
# #     def language(self):
# #         print("English")
# #     def type(self):
# #         print("Developed")

# # obj1 = India()
# # obj2 = USA()

# # for i in (obj1, obj2):
# #     i.capital()
# #     i.language()
# #     i.type()



# class Bird:
#     def wings(self):
#         print("Bird has two wings")
#     def eyes(self):
#         print("Bird has two eyes")
#     def fly(self):
#         print("Most of the birds can fly")

# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow can fly")

# class Ostrich(Bird):
#     def fly(self):
#         print("Ostrich can not fly")


# bird = Bird()
# sparrow = Sparrow()
# ostrich = Ostrich()

# bird.eyes()
# bird.wings()
# bird.fly()
# ostrich.fly()







#Create a Car class without any variables and methods
# class car:
#     pass

# Create a child class Bus that will inherit all the variables and methods of Vehicle class

# class Vehicle:
#     def __init__(self, name, milage):
#         self.name = name
#         self.milage = milage

# class Bus(Vehicle):
#     pass


# obj = Bus("ABC",10)

# print(obj.milage, obj.name)



