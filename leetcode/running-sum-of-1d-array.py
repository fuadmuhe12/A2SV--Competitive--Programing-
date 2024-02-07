class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j = 0 
        arr = []
        for i in nums:
            j += i
            arr.append(j)
        return arr
            
        