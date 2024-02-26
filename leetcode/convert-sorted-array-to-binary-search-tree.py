# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(left, right):
            if left > right:
                return 
            mid = (left +right)//2
            root = TreeNode()
            root.val = nums[mid]
            root.right = rec(mid+1, right)
            root.left = rec(left, mid-1)
            return root
        return rec(0, len(nums)-1)
