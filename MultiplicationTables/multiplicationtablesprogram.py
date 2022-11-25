N=int(input("Enter the Value Of N: "))
def MultiplicationTables(x):
    for i in range(2,N+1):
        
        for j in range(1,13):
            
            print(i," x ",j," = ",i*j)

        print("")
MultiplicationTables(N)