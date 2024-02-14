class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        prex = 0
        start = 0
        patch = 0
        while True:
            cur =  prex +1 
            if start < len(nums)  and nums [start ] <= cur:
                prex += nums[start]
                start += 1
            else:
                patch += 1
                prex += cur
                
            if prex >=n:
                return patch

