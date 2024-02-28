# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def back(root):
            f =  None
            mn = float('inf')
            mx = float('-inf')
            if root:
                f = root.val
            def rec(root):
                nonlocal mn, mx
                
                if root:
                    mx = max(mx, root.val)
                    mn = min(mn, root.val)
                    rec(root.left)
                    rec(root.right)
            rec(root)
            return max(abs(mx - f ), abs(mn - f))
        mt = float('-inf')
        def s(root):
            nonlocal mt
            if root:
                mt = max(back(root), mt)
                s(root.left)
                s(root.right)
        s(root)
        return mt

            
            



            

                
        
