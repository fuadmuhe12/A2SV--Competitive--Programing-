# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mas = float('-inf')
        def rec(root):
            nonlocal mas
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
                sums = 0
                if  val:
                    sums += root.val
                    if left:
                        sums += left[3] 
                    if right:
                        sums += right[3]
                    
                 
                    mas = max(sums,mas)

                
                
                # if left and  left[2] and right[2] and val:
                #     sums += root.val + left[3] + right[3]
                #     mas =  max(sums, mas)
                min_ = min( mn, rmn, root.val)
                max_ = max( mx , rmx, root.val)
                return [max_ if max_ != float('-inf') else root.val , min_ if min_ != float('inf') else root.val  , val, sums]
        rec(root)
        return mas if mas> 0 else 0

   

        