


class A:
    def __init__(self):
        print("Init of class A")

    def method1(self):
        print("This is method 1")
    
    def method2(self):
        print("This is method 2")

class B():
    def __init__(self):
        #super().__init__()
        print("Init of class B")
    def method3(self):
        print("This is method 3")

    def method4(self):
        print("This is method 4")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("Init of C")
    def method5(self):
        print("This is method 5")

obj = C()
