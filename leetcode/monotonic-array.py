class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        else:
            if nums[-1] >= nums[0]:
                for i in range(1, len(nums)):
                    if nums[i] < nums[i-1]:
                        return False
                else:
                    return True
            else:
                for i in range(1, len(nums)):
                    if nums[i] > nums[i-1]:
                        return False
                else:
                    return True