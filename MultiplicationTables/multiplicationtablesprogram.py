class Project:
    N=int(input("Enter the Value Of N: "))
    def MultiplicationTables(x):
        k=int(input("Enter the desired number of values you want in the Tables : "))
        for i in range(2,x.N+1):
          print("\nMultiplication Table of",i,"\n")
        
          for j in range(1,k):
            
            print(i," x ",j," = ",i*j)

Project.MultiplicationTables=classmethod(Project.MultiplicationTables)
print("Multiplication Tables")
Project.MultiplicationTables()
