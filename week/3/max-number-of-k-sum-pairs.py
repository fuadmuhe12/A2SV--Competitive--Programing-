class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        1. sort the arry  and then have a left and right pointer  if the sum of the two is equal to k move inside , if it less move the left if is more move the right the do this untill while left < right

        '''
        nums.sort()
        l = 0
        r = len(nums)-1
        tot = 0
        while r > l:
            if nums[r] + nums[l] == k:
                tot += 1
                r -= 1
                l += 1
            elif nums[r] + nums[l] > k:
                r -= 1
            else:
                l += 1
        return tot

            