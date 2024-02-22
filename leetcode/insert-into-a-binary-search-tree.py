# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node =  TreeNode(val)

        def ins (root, prev = None):
            if root:
                if root.val > val:
                    prev = root
                    ins(root.left, prev)
                else:
                    prev = root
                    ins(root.right, prev)
            elif prev:
                if prev.val > val:
                    prev.left  = node
                else:
                    prev.right = node
            else:
                root = node
                return root
        ins(root)
        return root if root else node

