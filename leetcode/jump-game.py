class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end =  len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= end:
                end = i
        
        if end == 0:
            return True
        else:
            return False