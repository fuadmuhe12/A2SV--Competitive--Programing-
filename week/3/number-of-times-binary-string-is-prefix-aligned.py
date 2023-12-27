class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mn =0
        sums = 0
        ans = 0
        for i in flips:
            sums += i
            mn = max(i, mn)
            if sums == (mn*(mn+1))/2:
                ans += 1
        return ans
