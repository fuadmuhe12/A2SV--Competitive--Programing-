# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root:
        #     stack = [root]
        # else:
        #     stack = []
    
        # ans = 0
        # vis = set()
        # while stack:
        #     while stack[-1].left and stack[-1].left not in vis :
        #         vis.add(stack[-1].left)
        #         stack.append(stack[-1].left)
        #         ans = max(ans, len(stack))
        #     while stack[-1].right and stack[-1].right not in vis :
        #         vis.add(stack[-1].right)
        #         stack.append(stack[-1].right)
        #         ans = max(ans, len(stack))
        #     ans = max(ans, len(stack))
        #     stack.pop()
        # return ans

        def rec (root):
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            return 1 + max(right, left)
            

           

        return rec(root) if root else 0




            

        

        