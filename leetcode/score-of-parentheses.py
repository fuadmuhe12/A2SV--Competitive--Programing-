class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack  = 0
        ans = 0
        for ind, val in enumerate(s):
            if val == '(':
                stack += 1
            else:
                stack -= 1
                if  s[ind-1] == '(':
                    ans +=  2**stack if stack else 1

                    
        return ans