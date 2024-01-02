class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 1
        while end < len(nums) and start < len(nums):
            if nums[start] != 0:
                start += 1
                end += 1
                continue
            if  nums[end] !=0:
                nums[end], nums[start] = nums[start], nums[end]
                start += 1
            end += 1
         
            


