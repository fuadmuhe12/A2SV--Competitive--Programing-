class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for start, val in enumerate(nums):
   
            vis = set()
            
            while nums[start]*val > 0 and (start != (start + nums[start])% len(nums)): 
                if len(vis) > 1 and  start in vis:
                    return(True)
                
                vis.add(start)
                start += nums[start]
                start %= len(nums)
                
                
        else:
            return False