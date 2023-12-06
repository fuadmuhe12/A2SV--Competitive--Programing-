class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        op = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]  :
                if op < 1:
                    op +=1
                    if i<2 or nums[i-2] <= nums[i]:
                        cur = nums[i] 
                    elif i+1 < len(nums) and nums[i-1] <= nums[i+1] or i+1 >= len(nums) :
                        cur = nums[i-1]
                    else:
                        return False
                else:
                    return False
            else:
                if nums[i] < cur:
                    return False
                cur = nums[i]
                pass
        return True

