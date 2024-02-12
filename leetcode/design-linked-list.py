class Node:
    def __init__(self, val):
        self.val = val
        self.next  = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail =None
        self.len = 0

    def get(self, index: int) -> int:
       
       
        if index > self.len-1 or index < 0:
            return -1
        count = 0
        cur = self.head
       
        while count < index:
            
            cur = cur.next
            count += 1
        return cur.val

    def arr(self):
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur =  cur.next
        return arr
        

    def addAtHead(self, val: int) -> None:

        node =  Node(val)
        node.next = self.head
        self.head = node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        node =  Node(val)
        dum = Node("dum")
        dum.next = self.head
        prev = dum
        cur =  self.head
        ind =  self.len  if self.head else 0
        count = 0
        while count < ind:
            prev = cur
            cur = cur.next
            count += 1
        node.next = cur
        prev.next = node
        self.head = dum.next 
        dum.next = None
        self.len += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len or index < 0:
            return 
        node =  Node(val)
        dum = Node("dum")
        dum.next = self.head
        prev = dum
        cur =  self.head
        ind =  index
        count = 0
        while count < ind:
            prev = cur
            cur = cur.next
            count += 1
        node.next = cur
        prev.next = node
        self.head = dum.next 
        dum.next = None
        self.len += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.len-1 or index < 0:
            return 
        dum = Node("dum")
        dum.next = self.head
        prev =  dum
        cur =  self.head
        count = 0
        while count< index:
            prev = cur
            cur = cur.next
            count += 1
        prev.next =  cur.next
        cur.next = None
        self.head= dum.next
        self.len -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)