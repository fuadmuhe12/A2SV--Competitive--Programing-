class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rem = []
        stack = []
        for ind, val in enumerate(s):
            if val == '(' or val == ')':
                if val == '(':
                    stack.append(ind)
                else:
                    if stack:
                        stack.pop()
                    else:
                        rem.append(ind) 
        if stack:
            rem.extend(stack)
        final = ''
        start = 0
        for ind, val in enumerate(s):
            if start< len(rem) and rem[start] == ind:
                start += 1
                continue
            else:
                final += val
        return final




    

                

