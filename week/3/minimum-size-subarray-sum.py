from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        n = len(nums)
        m = float('inf')
        s = nums[start]

        while end < n and start <= end:
            if s >= target:
                m = min(m, end - start + 1)
                s -= nums[start]
                start += 1
            elif s < target:
                end += 1
                if end < n:
                    s += nums[end]

        return m if m != float('inf') else 0
