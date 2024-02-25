class Solution:    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #u_g
        def add(node):
            cur = self.an
            while(cur):
                if(cur.val < node.val):
                    prev = cur
                    cur = cur.next
                else: break
            node.next, prev.next = prev.next, node
        self.an = ListNode(-5001)
        while(head):
            temp, head = head, head.next
            temp.next = None
            add(temp)
        return self.an.next