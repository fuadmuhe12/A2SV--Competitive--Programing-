# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        prev = None
        while cur.next:
            nex =  cur.next
            cur.next = prev
            prev=  cur
            cur=  nex
        cur.next =  prev
        ans = 0
        val = 1
        while cur:
            ans += cur.val * val
            cur =  cur.next
            val *= 2
        return ans

            