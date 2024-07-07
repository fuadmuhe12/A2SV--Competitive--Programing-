# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        start = 0
        end  =  len(nums)-4
        minval = float("inf")
        while end < len(nums):
            minval = min(nums[end] -nums[start], minval)
            start += 1
            end += 1
        return minval