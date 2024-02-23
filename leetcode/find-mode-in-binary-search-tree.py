# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict
        tre = defaultdict(int)
        def dt(root):
            if root:
                tre[root.val] += 1
                dt(root.left)
                dt(root.right)
        dt(root)
        print(tre)
        mx = 0
        curmx = []
        print(tre.keys())
        for i in tre.keys():
            if tre[i] > mx:
                mx = tre[i]
                curmx.clear()
                curmx.append(i)
            elif tre[i] == mx:
                curmx.append(i)
        return curmx




        