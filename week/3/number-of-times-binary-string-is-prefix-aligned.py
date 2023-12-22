class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mn = 0
        ones = 0
        ans = 0
        for i in range(len(flips)):
            ones += 1
            mn = max(flips[i], mn)
            if ones == mn:
                ans += 1
        return ans

