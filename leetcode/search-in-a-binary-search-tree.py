# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def rec(root, val):
            if root:
                if root.val == val :
                    return root
                elif root.val > val:
                    return rec(root.left, val)
                else:
                    return rec(root.right, val)
            return None
        return rec(root, val)