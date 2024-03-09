class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for ind, i in enumerate(nums):
           ans.extend(list (map(int, str(i))))
        return ans