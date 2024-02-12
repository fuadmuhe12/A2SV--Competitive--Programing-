# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def rev(node):

            if node.next:
                val, last = rev(node.next)
                val.next = node
                node.next = None
            elif not node.next:
                last = node
          
            return[ node, last]
        return rev(head)[1]
        
