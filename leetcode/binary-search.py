class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bi(left, right):
            if left > right :
                return -1
            mid =  (left+ right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bi(left, mid-1)
            else:
                return bi(mid+1, right)
        return bi(0, len(nums)-1)

