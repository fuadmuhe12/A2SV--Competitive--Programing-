class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c= Counter(nums)
        ans = []
        for key in c.keys():
            if c[key] > len(nums)//3:
                ans.append(key)
        return ans