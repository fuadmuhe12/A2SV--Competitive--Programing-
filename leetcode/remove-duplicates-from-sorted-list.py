# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        cur = head
        dum =  ListNode("dum")
        dum.next = head
        prev = dum
        while cur:
            if cur.val in seen:
                cur = cur.next
                
                continue
            else:
                seen.add(cur.val)
                prev.next = cur
                prev = cur
                cur = cur.next
        prev.next = None
        return head



