class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        count =  Counter(list(s))
        used = {}
        for ind , val in enumerate(s):
            while stack and stack[-1] > val and val not in used:
                if count[stack[-1]] > 0:
                    c = stack.pop()
                    del used[c]
                else:
                    break
            if val not in used:
                stack.append(val)
                used[val] = 0
            count[val] -=1
        return "".join(stack)
                
