class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        0 0 1 1 2 2
              i   j
        
        """
        for left in range(len(nums)-1):
            right = left +1 
            if nums[left] == 0:
                continue
            else:
                while right < len(nums):
                    if nums[right] < nums[left]:
                         nums[right] ,nums[left] = nums[left],  nums[right] 
                    right += 1
                    
        
 


        