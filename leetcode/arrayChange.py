class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        val = 0 
        for i in nums:
            dic[i] = val
            val += 1

        for i in operations:
            ind = dic[i[0]]
            del dic[i[0]]
            dic[i[1]] = ind
            nums[ind] = i[1]
        return nums
