class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        fix = defaultdict(int)
        fix[0] = 1
        count = 0
        cur = 0

        for i in nums:
            cur += i
            if cur - k in fix:
                count += fix[cur - k]
            fix[cur] += 1
        return count
