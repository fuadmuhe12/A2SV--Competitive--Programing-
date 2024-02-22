class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(h1, h2, prev = None, head = None):
            if h1 and h2:
                if h1.val < h2.val:
                    if not head:
                        head = h1
                    if prev:
                        prev.next = h1
                    prev =  h1
                    rec(h1.next,h2 , prev, head)
                else:
                    if  head == None:
                        head = h2
                    if prev:
                        prev.next = h2
                    prev =  h2
                    rec(h1, h2.next, prev, head)
                return head 
            elif h1:
                if prev:
                    prev.next = h1
                else:
                    head =  h1
            else:
                if prev :
                    prev.next =  h2
                else:
                    head =  h2
            return head 

        return  rec(list1, list2)


                    
