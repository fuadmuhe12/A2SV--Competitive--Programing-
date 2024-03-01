# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inord(cur):
            if cur:
                inord(cur.left)
                arr.append(cur.val)
                inord(cur.right)
        inord(root)
        print(arr)
        def cons(left, right):
            if left > right:
                return 
            mid = (left + right)//2
            root = TreeNode(arr[mid], cons(left, mid-1) ,cons(mid+1, right))
            return root
        return cons(0, len(arr)-1)