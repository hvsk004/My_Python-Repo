n=int(input())
x=1+(n-1)*2
frame=[[n for i in range(x)] for i in range(x)]
for i in frame:
    print(i)
for i in range(n-1)