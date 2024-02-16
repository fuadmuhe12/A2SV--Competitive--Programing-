class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        end = 0
        start = 0
        while end < len(path):
            while end  < len(path) and path[end] == '/':
                end += 1
            cur = ''
            while end < len(path) and  path[end] != '/':
                cur += path[end]
                end +=1
            if cur != ".." and cur !=  "." :
                if  cur  != "":
                    stack.append('/'+ cur) 

            elif cur == ".." and stack:
                stack.pop()
        return '/' if not stack  else "".join(stack)