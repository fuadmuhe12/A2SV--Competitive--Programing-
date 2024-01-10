class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        start = 0
        end = len(nums)-1
        ans = 0
        while end > start:
            if nums[start] + nums[end] < target:
                ans += end - start
                start += 1  
            elif nums[start] + nums[end] >= target:
                end -= 1
        return ans
            

        
            
