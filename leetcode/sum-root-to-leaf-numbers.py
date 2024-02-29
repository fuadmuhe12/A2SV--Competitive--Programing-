# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        stack = []
        def rec(root):
            nonlocal ans
            if root:
                stack.append(root.val)
                if not root.right and not root.left:
                    ans.append(stack[:])
                else:
                    rec(root.left)
                    rec(root.right)
                stack.pop()
        
        rec(root)
        ans = ["".join(map(str, i)) for i in ans ]
       
        return list(accumulate(list(map(int, ans))))[-1] if ans else  0
