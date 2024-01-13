class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]

        max_sum = cur_sum
        start = 0
        end = k
        while end < len(nums):
            cur_sum = cur_sum - nums[start] + nums[end]
            max_sum = max(cur_sum, max_sum)
            start += 1
            end += 1
        return max_sum /k
       