class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        end = 0
        start = 0
        le  = 0
        re = 0
        odd = 0
        ans = 0
        change = True
        while change :
            change = False
            re = 0
            while end  < len(nums) and odd <= k:
                if nums[end]% 2 and odd < k :
                    odd += 1
                elif  odd == k  and nums[end] % 2:
                    break
                
                if odd == k  and nums[end] % 2 ==  0:
                    re += 1
                
                end += 1
                    
            if odd >= k :
                change = True
                le = 0 
                while   odd == k:
                    if nums[start] % 2:
                        odd -=1 

                    else:
                        le += 1
                    start += 1
                ans += (le + 1) * (re + 1)
        return ans
        

                 


                


