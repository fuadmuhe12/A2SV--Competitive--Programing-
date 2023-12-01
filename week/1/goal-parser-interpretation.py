class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        stack = []
        start = 0
        while start <len(command):
            stack.append(command[start])
            
            if stack == ["G"]:
                ans += "G"
                stack .clear()
            elif stack == ["(",")"]:
                ans += "o"
                stack.clear()
            elif stack == ["(","a","l",")"]:
                ans += "al"
                stack.clear()
            start += 1
        return ans


