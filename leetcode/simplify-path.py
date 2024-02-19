class Solution:
    def simplifyPath(self, path: str) -> str:
       stack = []
       for i in path.split('/'):
           if i == '' or i == '.':
               continue
           if i == '..':
               if stack:
                   stack.pop()
               continue
        
           stack.append(i)
       return '/' + '/'.join(stack)