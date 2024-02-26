# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(root, arr):
            print(arr)
            if root:
                arr.append(root.val)
                arr = rec(root.left, arr)
                arr = rec(root.right, arr)
            arr.append('-1')
            return arr

        return  rec(p, []) == rec(q, [])
