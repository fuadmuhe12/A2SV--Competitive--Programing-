class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = 0
        vol = ("a", "e", "i", "o", "u")
        maxs = 0
        cur = 0
        while end < len(s):
            if s[end] in vol:
                cur += 1
            maxs = max(maxs, cur)
            if end +1 - start == k:
                end += 1
                if s[start] in vol:
                    cur -= 1
                start += 1
            else:
                end += 1
        return maxs
            



