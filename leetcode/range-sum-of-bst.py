# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def rec(root):
            nonlocal ans
            if root:
                if low <= root .val <= high:
                    ans += root.val
                rec(root.right)
                rec(root.left)
        rec(root)
        return ans