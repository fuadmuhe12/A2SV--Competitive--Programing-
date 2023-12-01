class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        start = 0
        ans = ''
        while start < m:
            ans += word1[start]
            if start < n:
                ans += word2[start]
            start += 1
        if start < n:
            ans += word2[start : n]
        return ans
