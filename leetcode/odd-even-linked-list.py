class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #u_s

        if(not head): return head
        od = head
        ev = head.next
        evh = ev
        while(ev and od and ev.next and od.next):
            od.next = ev.next
            od = od.next
            ev.next = od.next
            ev = ev.next
        od.next = evh
        return head