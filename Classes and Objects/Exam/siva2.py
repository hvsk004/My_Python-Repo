class A:
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is the 2nd Method")
obj=A()
class B(A):
    def method3(self):
        print("This is method 3")
    def method4(self):
        print("This is method 4")
obj2=B()
obj2.