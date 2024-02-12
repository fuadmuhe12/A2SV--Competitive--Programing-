# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if count%2:
            ind = count//2 
            cur =  head
            for i in range(ind):
                cur = cur.next
            return cur
        else:
            ind = count//2
            cur = head
            for i in range(ind):
                cur = cur.next
            return cur
