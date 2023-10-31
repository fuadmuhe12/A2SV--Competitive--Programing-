class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        canonical_path = '/' + '/'.join(stack) if stack else '/'
        return canonical_path
