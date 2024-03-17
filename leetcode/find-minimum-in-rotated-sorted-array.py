class Solution:
    def findMin(self, nums: List[int]) -> int:
        cur =  nums[-1]
        low = 0
        high = len(nums)-1

        while low <= high:
            mid =  (low + high)//2

            if nums[mid] <= cur:
                cur = nums[mid]
                high = mid -1
            else:
                low = mid +1
        return cur