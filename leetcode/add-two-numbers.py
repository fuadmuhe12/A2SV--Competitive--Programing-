# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1 = ''
        v2 = ''
        cur1  = l1
        while cur1:
            v1 += (str(cur1.val))
            if cur1.next:
                cur1 = cur1.next
            else:
                break
        print('v1', v1)
        cur2 = l2
        while cur2:
            v2 += (str(cur2.val))
            if cur2.next:
                cur2 = cur2.next
            else:
                break
        print('v2', v2)
        final = int(v1[::-1]) + int(v2[::-1])
        final = str(final)[::-1]
        print('f', final)
        k = ListNode(final[0]) 
        q = k
        for i in final[1:]:
            node = ListNode(i)
            k.next = node
            k = node
        return q
            
