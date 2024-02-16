class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)

        for ind , val in enumerate(temperatures):
            if not stack :
                stack.append([ind, val])
            else:
                while stack and val > stack[-1][-1]:
                    ans[stack[-1][0]] = ind - stack[-1][0] 
                    stack.pop()
                stack.append([ind, val])
        return ans

