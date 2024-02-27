import numpy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def backtrack(index):

            if index >= len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
            backtrack(index + 1)
            
        backtrack(0)
        return ans