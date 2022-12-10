def div(a,b):
    return a/b
def betterdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=betterdiv(div)
a=div(4,2)
print(a)