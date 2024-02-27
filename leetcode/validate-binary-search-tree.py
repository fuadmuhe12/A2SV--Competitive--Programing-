# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root):
            if root:
                left =  rec(root.left)
                right = rec(root.right)
                val = True
                mn = float("inf")
                mx = float('-inf')
                rmn = float("inf")
                rmx = float('-inf')
                if left:
                    mn = min(left[1], mn)
                    mx = max(left[0], mx)
                    if left[2] and mx < root.val:
                        val = True
                    else:
                        val = False
                if val:
                    if right:
                        rmn = min(right[1], rmn)
                        rmx = max(right[0], rmx)
                        if right[2] and rmn > root.val:
                            val = True
                        else:
                            val = False
                
                min_ = min( mn, rmn, root.val)
                max_ = max( mx , rmx, root.val)
                return [max_ if max_ != float('-inf') else root.val , min_ if min_ != float('inf') else root.val  , val]
        def recR(root):
            if root:
                left =  rec(root.left)
                right = recR(root.right)
                val = True
                if left:
                    if left[1] and left[0] < root.val:
                        val = True
                    else:
                        val = False
                if val:
                    if right:
                        if right[1] and right[0] > root.val:
                            val = True
                        else:
                            val = False
                return [left [ 0] if left else root.val , val]

        return rec(root)[2]




                


           