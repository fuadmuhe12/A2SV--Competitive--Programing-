# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que =  deque()
        que.append(root) if root else []
        ans = []
        while que:
            level = []
            cur = []
            for i in que:
                if i.right:
                    level. append(i.right)
                if i.left:
                    level.append(i.left)
                cur.append(i.val)
            ans.append(cur)
            que =  deque(level)
        return [ val[::-1] if not ind%2 else val for ind, val in enumerate(ans) ]



                
        

