class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = set(['*', '/', '+', '-'])
        for i in tokens:
            if i in val:
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                if i == '/':
                    ans = math.ceil(v2 /v1) if v2/v1 < 0 else math.floor(v2 /v1)
                else:
                    ans = eval(f' {v2} {i} {v1}')
                stack.append(ans)
            else:
                stack.append(i)
        return int(stack[0])

