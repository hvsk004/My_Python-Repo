rows=5
for i in range(rows,0):
    for j in range(i+1,0):
        print(j,end="")
        j-=1
    i-=1
    print("")