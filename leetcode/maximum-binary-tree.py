# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
            
        
        def conqure(cur):
            if not cur:
                return 
            ind = cur.index(max(cur))
            node = TreeNode(cur[ind])
            node.left = conqure(cur[:ind])
            node.right = conqure(cur[ind+1:])
            return node
        return conqure(nums)

            


