n=int(input("Enter the Value of n "))
m=n//4
q=n/2
y=0
t=0
#Initiating a magicSquare with all elements as zeroes
magicSquare = [[0 for i in range(n)] for i in range(n)]
#Defining Functio to generate a doubly even(n%4==0) magic square
def genDoublyEvenMagicSquare(x):
    p=1
    m=x//4
    for i in range(0,x):
        for j in range(0,x):
            if i<m and j<m:#Top Left Corner
                magicSquare[i][j]=p
            elif x-1-i<m and x-j-1<m:#Bottom Right Corner
                magicSquare[i][j]=p
            elif x-i-1<m and j<m:#Bottom Left Corner
                magicSquare[i][j]=p
            elif i<m and x-j-1<m:#Top Right Corner
                magicSquare[i][j]=p
            elif i>=m and x-i-1>=m and j>=m and x-j-1>=m:#Middle Segment
                magicSquare[i][j]=p
            else:#The rest of the magicSquare
                magicSquare[i][j]=x*x+1-p
            p+=1
            for i in range(0,n):#For loop to print the 2D array in the form of a matrix
                for j in range(0,n):
                    print('%2d ' % (magicSquare[i][j]),end='')
                    if j==n-1:
                       print()
k=(n*(n*n)+1)/2
def OddMagicsquare(x): #Defining a function to create a magic square
    i=n//2  #Intializing Position of 1
    j=n-1   #Intializing Position of 1
    num=1
    while num<=(n*n):
        if i==-1 and j==n:
            i=0
            j=n-2
        else:
            
            if j==n:
                j=0
            if i<0:
                i=n-1
        if magicSquare[int(i)][int(j)]:
            i=i+1
            j=j-2
            continue
        else:
            magicSquare[int(i)][int(j)]=num
            num=num+1
        i=i-1
        j=j+1
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),end='')
            if j == n - 1:
                print()
    return magicSquare
def Oddmagic2(n):
    r=0
    c=n//2
    x=0
    z=int(n*n)
    for x in range(1,z+1):
        magicSquare[int(r)][int(c)]=x
        if x%n==0:
            r+=1
        else:
            r-=1
            c-=1
            if r<0:
                r+=n
            if c<0:
                c+=n
    return magicSquare

def SinglyEvenMagicSquare(x,q):
    magicSquare=Oddmagic2(int(q))#Filling the First Quadrant by calling OddMagicsquare Function
    for i in range(0,int(int(q))):
        for j in range(0,int(int(q))):
            magicSquare[i+int(q)][j+int(q)]=magicSquare[i][j]+int(q)*int(q)#Filling the Second Quadrand
            magicSquare[i][j+int(q)]=magicSquare[i][j]+int(q)*int(q)*2#Filling the third Quadrant
            magicSquare[i+int(q)][j]=magicSquare[i][j]+int(q)*int(q)*3#Filling the Fourth Quadrant

    for i in range(0,int(q)):
        for j in range(0,int(q)/2):#For loop to interchange first and fourth quadrant
            if i==int(q)/2:
                y=j+1
            else:
                y=j
            t=magicSquare[i][y]
            magicSquare[i][y]=magicSquare[i+int(q)][y]
            magicSquare[i+int(q)][y]=t
        for j in range(n-int(q)/2+1,n):
            t=magicSquare[i][j]
            magicSquare[i][j]=magicSquare[i+int(q)][j]
            magicSquare[i+int(q)][j]=t
    # for i in range(0, n):
    #     for j in range(0, n):
    #         print('%2d ' % (magicSquare[i][j]),end='')
    #         if j == n - 1:
    #             print()
SinglyEvenMagicSquare(6,q)


