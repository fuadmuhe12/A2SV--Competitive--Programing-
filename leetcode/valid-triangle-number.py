class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        nums.sort()
        def search(start, end, tar, nums):
            if start <= end:
                mid = (start + end) // 2
                if nums[mid] == tar and mid-1 >= start and nums[mid-1] != tar:
                    return mid
                elif nums[mid] > tar or nums[mid] == tar:
                    return search(start, mid - 1, tar, nums)
                elif nums[mid] < tar :
                    return search(mid + 1, end, tar, nums)
            # If the target is not found, return the index of the next greater element if it exists
            return start if start < len(nums) and nums[start] >= tar else -1
        print(search(0, len(nums)-1, 7, nums))

        for end in range(len(nums)-1, 1, -1):
            for start in range(0, end-1):
                mid =  search(start+1, end-1, nums[end] - nums[start] +1, nums)
                if mid >0:
                    ans += end - mid
        return ans


