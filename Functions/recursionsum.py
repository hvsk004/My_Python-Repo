x=int(input(""))
def recur_sum(n):
   if n==0:
       return n
   return n+recur_sum(n-1)
ans=recur_sum(4)
print(ans)
   