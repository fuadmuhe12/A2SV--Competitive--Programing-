# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        while n > 0:
            cur = cur.next
            n -= 1
        dum = ListNode("dum")
        dum.next =head
        prev = dum
        back = head
        while cur:
            cur = cur.next
            prev = back
            back =back.next 
        
        prev.next = back.next
        head = dum.next
        back.next = None
        return head

            

        