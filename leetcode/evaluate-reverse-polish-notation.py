class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i in ["+", "/", "*", "-"]:
                v2 =int(stack.pop())
                v1 = int(stack.pop())
                if i == "+":
                    s= v1 + v2
                elif i == "-":
                    s = v1-v2
                elif i =="/":
                    s = int(v1/v2)
                elif i == "*":
                    s = v1 *v2
                stack.append(s)
            else:
                stack.append(i)
        return stack[0]