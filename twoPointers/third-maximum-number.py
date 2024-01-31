class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = set()
        for ind, val in enumerate(nums):
            n.add(val)
            if len(n) >= 3:
                return nums[ind]
            
        return nums[0]