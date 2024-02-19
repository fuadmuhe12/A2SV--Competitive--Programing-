class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = {'[':']' , '{':'}', '(':')'}
        dic = {']':'[' , '}':'{', ')':'('}
        for i in s:
            if i in op:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if dic[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        return not stack

                    

            
        