# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int, dep = 0) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dum = ListNode(next=head)
        prev = dum
        cur = head

        while cur:
            dep += 1

            if left <= dep < right:
                nextNode = cur.next
                cur.next = nextNode.next
                nextNode.next = prev.next
                prev.next = nextNode
            else:
                if dep < right:
                    prev = prev.next
                cur = cur.next

        return dum.next

        

        
        