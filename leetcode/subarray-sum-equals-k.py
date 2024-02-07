class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        edge:
         if len(nums) = 1
        """
        dic_freq = defaultdict(int)
        dic_freq [0] = 1
        acc = 0
        ans = 0
        for ind, val in enumerate(nums):
            acc += val
            if acc -k in dic_freq:
                ans += dic_freq[acc-k]
            dic_freq[acc] += 1
            
        return ans

