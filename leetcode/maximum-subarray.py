class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        seg = float("-inf")
        acc = 0
        min_prex = 0
       
        for i in nums:
            acc += i
            seg = max(seg, acc - min_prex)
            min_prex = min(min_prex, acc)
        return seg
