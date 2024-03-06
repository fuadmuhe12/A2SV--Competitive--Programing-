class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        min_ = float('inf')
        start , end =0, len(nums)-3
        while end < len(nums):
            min_ = min(min_, abs(nums[start]-nums[end]))
            end += 1
            start += 1
        return min_
