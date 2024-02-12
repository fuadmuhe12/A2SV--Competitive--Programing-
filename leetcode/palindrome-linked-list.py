# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        odd = True if count % 2 else False
        cur = head
        for i in range(count//2):
            cur =  cur.next
        re = cur.next if odd else cur # the parst to be reversed
    
        def reva(head):
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
        rev = reva(re) # reversed end part
        cur =  rev
        while rev:
            if rev.val != head.val:
                return False
            else:
                rev = rev.next
                head = head.next
        return True



       
      