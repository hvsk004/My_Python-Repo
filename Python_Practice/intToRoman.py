class Solution(object):
    def intToRoman(self, num):
         val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
         syb = ["M", "CM", "D", "CD","C","XC", "L", "XL","X", "IX", "V", "IV","I"]
         roman_num = ''
         i=0
         while num>0:
             for _ in range(num//val[i]):
                 roman_num+=syb[i]
                 num-=val[i]
             i+=1
         print(roman_num)
num = int(input("num = "))
Ans=Solution()
Ans.intToRoman(num)