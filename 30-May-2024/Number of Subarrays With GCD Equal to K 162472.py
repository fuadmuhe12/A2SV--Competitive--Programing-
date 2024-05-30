# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        lenVal = len(nums)
        val = 0;j = 0;answer = 0
        
        while(val<lenVal):
            #print(gcd)
            gcd = nums[val]
            for j in range(val,lenVal):
                gcd = GCD(nums[j],gcd)
                if(gcd==k):
                    answer+=1
                elif(gcd<k):
                    break
            val+=1
        return answer
            
            
def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)
            