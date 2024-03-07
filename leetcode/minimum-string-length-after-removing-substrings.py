class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            stack.append(i)
            while len(stack) > 1:
                if f'{stack[-2]}{stack[-1]}' == 'AB' or f'{stack[-2]}{stack[-1]}' == 'CD':
                    stack.pop()
                    stack.pop()

                else:
                    break
        return len(stack)
                

            