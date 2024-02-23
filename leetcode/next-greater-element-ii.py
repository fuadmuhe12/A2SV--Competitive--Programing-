class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        maxStack = []
        nums =  nums + nums
        for ind, val in enumerate(nums):
            while maxStack  and maxStack[-1][-1] < val:
                if maxStack[-1][0] < n:
                    dic[maxStack[-1][0]] = val
                maxStack.pop()
            maxStack.append([ind, val])
            if ind < n:
                dic[ind] = -1
        return  [dic[i] for i in range(n)]

        






