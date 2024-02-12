# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur = head
        while cur:
            if cur.val == "1":
                return True
            else:
                cur.val = "1"
            cur = cur.next
        return False

