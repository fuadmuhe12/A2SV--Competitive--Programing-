class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #running sum
        cur = 0
        tot = sum(nums)
        for i in range(len( nums)):
            if cur == tot - cur- nums[i]:
                return i
            cur += nums[i]
        return -1