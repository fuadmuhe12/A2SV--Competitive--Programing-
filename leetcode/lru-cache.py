class Node :
    def __init__(self, key, vals):
        self.next = None
        self.prev = None
        self.val = [vals, key]

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store =  {}
        self.tail  = None
        self.head = None
    def  cur(self):
        cur =  self.head
        arr = []
        seen = set()
        while cur:
            if cur in seen:
                return ["seen", cur.val]
            seen.add(cur)
            
            arr.append(cur.val)
            cur = cur .next
        return arr


    def get(self, key: int) -> int:
        if key in self.store:
            elem =  self.store[key]
            if elem == self.tail:
                pass
            elif elem == self.head:
                self.rem(self.head)
                node = elem
                if self.tail:
                    self.tail.next = node
                    node.prev =  self.tail
                    node.next = None
                    self.tail =  node
                else:
                    node.prev =  self.tail
                    node.next = None
                    self.tail =  node
                    self.head =  node
            else:
                self.rem(elem)
                node = elem
                #add elem to end 
                if self.tail:
                    self.tail.next = node
                    node.prev =  self.tail
                    node.next = None
                    self.tail =  node
                else:
                    node.prev =  self.tail
                    node.next = None
                    self.tail =  node
                    self.head =  node
            # print(self.cur(), "get")
            return elem.val[0]
        else:
            # print(self.cur(), "get")
            return -1

    def rem(self, node):
        tail_dum =  Node("d", "d")
        self.tail.next =  tail_dum
        tail_dum.prev =  self.tail
        dum =  Node("d", "d")
        dum.next =  self.head
        self.head.prev = dum
        prev =  node.prev
        nex = node.next
        prev.next = nex
        if nex:
            nex.prev = prev
        node .prev =  node.next =  None
        if dum.next ==  tail_dum:
            self.head = self.tail = None
            return 
        self.head =  dum.next
        if self.head != tail_dum:
            self.head.prev = None
        

        #tail
        self.tail =  tail_dum.prev
        if self.tail != dum:
            self.tail.next = None


        

        



    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node. val = [value, key]
            self.rem(node)
            if self.tail:
                self.tail.next = node
                node.prev =  self.tail
                node.next = None
                self.tail =  node
            else:
                node.prev =  self.tail
                node.next = None
                self.tail =  node
                self.head =  node
        elif self.cap >0:
            node = Node(key, value)
            if self.tail:
                self.tail.next = node
                node.prev =  self.tail
                node.next = None
                self.tail =  node
            else:
                node.prev =  self.tail
                node.next = None
                self.tail =  node
                self.head =  node
            self.cap -=1 
            self.store[key] = node
        else:
            del self.store[self.head.val[1]]
        
            self.rem(self.head)
            
            node = Node(key, value)
            if self.tail:
                self.tail.next = node
                node.prev =  self.tail
                node.next = None
                self.tail =  node
            else:
                node.prev =  self.tail
                node.next = None
                self.tail =  node
                self.head =  node
            self.store[key] = node





       


        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(self.acity)
# param_1 = obj.get(key)
# obj.put(key,value)