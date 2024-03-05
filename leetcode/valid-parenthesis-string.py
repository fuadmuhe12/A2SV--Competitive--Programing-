class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        stack = []
        for ind, i in enumerate(s):
            if i == '(':
                stack .append(ind)
            elif i == "*":
                star.append(ind)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        if len(stack) > len(star):
            return False
        while stack:
            v = stack.pop()
            p =  star.pop()
            if v > p:
                return False
        else:
            return True


