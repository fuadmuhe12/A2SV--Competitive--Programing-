# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        if len(nums) < 2:
            return 0
        else:
            for i in range(1, len(nums)):
                mx = max(mx, nums[i] -nums[i-1])
            return mx