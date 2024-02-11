class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        last = 0 #last added used elem
        sum_ = 0 #last sum
        ans = [0]*len(nums)
        for ind, val in enumerate(nums):
            sum_ +=  ind *(val - last)
            last = val
            ans[ind] += sum_
        ans = ans[::-1]
        last = 0 #last added used elem
        sum_ = 0 #last sum
        for ind, val in enumerate(nums[::-1]):
            sum_ +=   ind *(-val + last)
            last = val
            ans[ind] += sum_
        return ans[::-1]





