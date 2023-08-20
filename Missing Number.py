class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = [i for i in range(n+1)]
        for i in nums :
            if i in x:
                x.remove(i)
        return(x[0])
