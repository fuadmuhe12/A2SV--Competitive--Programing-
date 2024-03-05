class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in nums[0]:
            for arr in nums[1:]:
                if i not in arr:
                    break
            else:
                ans.append(i)
        return sorted(ans)