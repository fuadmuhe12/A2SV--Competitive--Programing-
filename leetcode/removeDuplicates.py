class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        val = []
        for i in nums:
            if i not in dic:
                dic[i] =True
                val.append(i)
        nums[:] = val
        return len(val)


