# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right = []
        left = []
        def rec(root, arr):

            if root:
                arr.append(root.val)
                arr = rec(root.left, arr)
                arr = rec(root.right, arr)
            arr.append("1")

            return arr
        def rec1(root, arr):

            if root:
                arr.append(root.val)
                arr = rec1(root.right, arr)
                arr = rec1(root.left, arr)
            arr.append("1")
            return arr
        
            
                

        if root:
            if root.left or root.right:
                
                lef =  rec(root.left, left) 
                rig =  rec1(root.right, right)
                print(lef)
                print(rig, 'r')

                return lef ==  rig
            else:
                return True
        else:
            return True
                