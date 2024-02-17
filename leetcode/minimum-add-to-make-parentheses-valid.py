class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        cl = 0
        ans = 0
        for i in s:
            if i == '(':
                op += 1
            else:
                if op > 0:
                    op -= 1
                else:
                    ans += 1
        ans += op
        return ans

