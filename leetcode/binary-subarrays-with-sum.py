class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic_freq = defaultdict(int)
        dic_freq [0] = 1
        acc = 0
        ans = 0
        for ind, val in enumerate(nums):
            acc += val
            if acc -goal in dic_freq:
                ans += dic_freq[acc-goal]
            dic_freq[acc] += 1
            
        return ans

