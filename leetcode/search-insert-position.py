class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        cur = high
        while low <= high :
            mid = (low + high)//2
            if mid >= len(nums) :
                break
            if nums[mid] < target:
                low = mid +1
            else:
                cur = mid
                high = mid -1
                
        return cur


                