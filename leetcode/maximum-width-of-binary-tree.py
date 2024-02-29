# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        use heap numbers to calculate the values for every level and calculate
        the di

        '''
        que = deque([[root, 1, 0]]) # root,  heap number ,  level
        maxwid = 0
        start_heap_number = 1

        prevLevel = 0
        while que:
            cur_root, heap, level =  que.popleft()
            if level > prevLevel:
                prevLevel =  level
                start_heap_number = heap
            maxwid =  max(maxwid, heap-start_heap_number +1)
            if cur_root.left:
                que.append([cur_root.left, 2*heap, level +1])
            if cur_root.right:
                que.append([cur_root.right, 2*heap +1, level +1])
        return maxwid







        