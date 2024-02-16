class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        end = 0
        start = 0
        while end < len(logs):
            
            cur = logs[end]
            if cur != "../" and cur !=  "./" :
                if  cur  != "":
                    ans += 1

            elif cur == "../" and ans > 0:
                ans -=1 
            end += 1
        return ans
