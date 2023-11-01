class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        prefix = defaultdict(int)
        prefix[0] = 1
        cur = 0
        ans = 0
        for i in nums:
            cur += i
            # Use modulo operator to calculate the remainder
            remainder = cur % k
            ans += prefix[remainder]
            prefix[remainder] += 1
        return ans
