class Car:
    wheels=4
    def __init__(self):
        self.company='BMW'
        self.mileage=10
        
car1=Car()
car2=Car()
print("Mileage of Car 1 is",car1.mileage,id(car1))
print("Mileage of Car 2 is",car2.mileage,id(car2))
#Instance Variables: If the value of the variable changes from object to object then those variables are called instance variables.
Car.wheels=5
print(car1.wheels)
print(car2.wheels)
#Static Variable: The variables which are shared by the whole class are known as static variables.
