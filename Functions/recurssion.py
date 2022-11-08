import sys 
sys.setrecursionlimit(2**12)
def hello():
    print("Hello World")
    hello()
hello()
print(sys.getrecursionlimit())
