class Solution:
    def largestOddNumber(self, num: str) -> str:
        ls = [i for i in range(len(num)-1, -1,-1)]
        for val in ls:
            print(val)
            if int(num[val]) % 2:
                return (num[:val+1])
                break
        else:
            return ""
          
        
       