class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        acc = 1
        for ind, val in enumerate(nums):
            acc *= val
            left[ind] = acc
        right = [0]*len(nums)
        cur = len(nums)-1
        acc= 1
        for ind, val in enumerate(nums[::-1]):
            acc *= val
            right[cur] = acc
            cur -= 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = right[i+1]
            elif i == len(nums)-1:
                ans[i] = left[i-1]
            else:
                ans[i] = left[i-1] * right[i +1]
        return ans


            
