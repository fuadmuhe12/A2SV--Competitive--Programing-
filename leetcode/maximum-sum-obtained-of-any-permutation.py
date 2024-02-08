class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        prex = [0]*len(nums)
        for start, end in requests:
            prex[start] += 1
            if end < len(nums)-1:
                prex[end +1] -= 1
        prefix = [0]*len(nums)
        acc = 0
        for ind, val in enumerate(prex):
            acc += val
            prefix[ind] = acc
        prefix.sort(reverse = True)
 
        sum_ = 0
        for i in range(len(nums)):
            sum_ += (prefix[i]*nums[i])
        return sum_%(10**9 + 7)




