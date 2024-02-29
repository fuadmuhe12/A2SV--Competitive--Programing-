class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.store = []

        

    def enQueue(self, value: int) -> bool:
        if len(self.store) < self.size:
            self.store.append(value)
            return True
        else:
            return False




        

    def deQueue(self) -> bool:
        if self.store:
            self.store.pop(0)
            return True
        else:
            return False

        

    def Front(self) -> int:
        return self.store[0] if self.store else -1
        

    def Rear(self) -> int:
        return self.store[-1] if self.store else -1
        

    def isEmpty(self) -> bool:
        return not self.store
        

    def isFull(self) -> bool:
        return len(self.store ) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()