class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        start = 0
        maxx = 0
        zeros_count = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zeros_count += 1

            while zeros_count > k:
                if nums[start] == 0:
                    zeros_count -= 1
                start += 1

            maxx = max(maxx, end - start + 1)

        return maxx-1