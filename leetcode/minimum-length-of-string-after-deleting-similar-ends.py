class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                break
            cur = s[start]
            for i in range(start, len(s)):
                if s[i] !=  cur:
                    break
            start = i
            for j in range(end, -1, -1):
                if s[j] != cur:
                    break
            end = j

            if s[start] != s[end]:
                break
        return end - start + 1  if end - start + 1 > 0 else 0