class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        alls = set(nums)
        n= len(alls)
        dic = {}
        end = 0
        ans = 0
        for start in range(len(nums)):
            while len(dic) < n and end < len(nums):
                dic[nums[end]] = end
                end += 1
            ans += len(nums)-end+1 if len(dic) >= n else 0
            if dic[nums[start]] == start:
                del dic[nums[start]]
        return ans
            


            

