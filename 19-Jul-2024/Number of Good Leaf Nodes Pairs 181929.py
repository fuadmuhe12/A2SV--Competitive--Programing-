# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def visit(current: TreeNode, counter: int) -> list:
            if not current:
                return []
            left = visit(current.left, counter + 1)
            right = visit(current.right, counter + 1)
            if not current.left and not current.right:
                return [counter]
            for l in left:
                for r in right:
                    if l + r - 2 * counter <= distance:
                        self.result += 1
            return left + right
        visit(root, 0)
        return self.result