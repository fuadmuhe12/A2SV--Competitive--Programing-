class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        use the remainder by storing it in the dictionary form their prefix sum

        '''
        dic_new = defaultdict(int)
        dic_new[0] += 1
        acc = 0
        ans = 0

        for ind, val in enumerate(nums):
            acc += val
            if acc % k in  dic_new:
                ans += dic_new[acc % k]
            dic_new[acc % k] += 1
        return ans
         
