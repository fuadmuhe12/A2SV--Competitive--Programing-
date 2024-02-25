# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        sm = []
        lg = []
        for i in l:
            if i<x:
                sm.append(i)
            else:
                lg.append(i)
        ans = sm+lg
        if ans==[]:
            return 
        head = temp = ListNode(ans[0])
        for i in range(1,len(ans)):
            temp.next = ListNode(ans[i])
            temp = temp.next
        return head