class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         dic =  defaultdict(int)
         mx =nums[0]
         for i in nums:
            dic[i] += 1
            if dic[i] > dic[mx]:
                mx = i 
         return mx


