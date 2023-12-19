class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        new = []
        ze = []
        while start < len(nums):
            if nums[start] != 0:
                new.append(nums[start])
            else:
                ze.append(nums[start])
            start += 1

        nums.clear()
        nums += new  + ze
        return nums


