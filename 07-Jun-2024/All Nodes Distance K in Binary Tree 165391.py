# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        final = []
        target = target.val
        def find(root):
            if not root:
                return None
            if root.val == target:
                curDiv(root.right, 1)
                curDiv(root.left, 1)
                return 1

            right = find(root.right)
            left = find(root.left)

            if right == k or left == k:
                final.append(root.val)
            elif right:
                curDiv(root.left, right + 1)
            elif left:
                curDiv(root.right, left + 1)

            return (right or left) + 1 if right or left else None 

        def curDiv(root, dist):
            if not root:
                return
            if dist == k:
                final.append(root.val)
                return
            curDiv(root.left, dist + 1)
            curDiv(root.right, dist + 1)

        find(root)
        return final