class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = 0
        a = 1
        while a < len(nums):
            
            while a< len(nums):
                
                if nums[m] + nums[a] == target:

                    return [m, a]
                a += 1
            m += 1
            a = m + 1
