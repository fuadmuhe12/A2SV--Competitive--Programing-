# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def rec(root, row, col):
            if root:
                dic[col].append([row, root.val])
                if root.left:
                    rec(root.left, row+1, col-1)
                if root.right:
                    rec(root.right, row+1, col+1)
        rec(root, 0, 0)

        key = list(dic.keys())
        key.sort()
        ans = []
        for i in key:
            ans.append([ans[1] for ans in sorted(dic[i])])
        return ans
