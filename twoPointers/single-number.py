class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cn = Counter(nums)
        for i in cn.keys():
            if cn[i] == 1:
                return i