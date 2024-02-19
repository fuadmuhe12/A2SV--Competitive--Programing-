class newQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.queue)

class MyStack:

    def __init__(self):
        self.cont1 = newQueue()
        self.cont2 = newQueue()
        

    def push(self, x: int) -> None:
        if self.cont2.is_empty() and self.cont1.is_empty():
            if self.cont2.is_empty():
                self.cont2.enqueue(x)
        elif self.cont2.is_empty():
            self.cont2.enqueue(x)
        else:
            self.cont1.enqueue(x)

    def pop(self) -> int:
        if self.cont2.is_empty() == self.cont1.is_empty() == True:
            return False
        elif self.cont1.is_empty() == True:
            if self.cont2.size() == 1:
                return self.cont2.dequeue()
            else:
                while self.cont2.size() > 1:
                    self.cont1.enqueue(self.cont2.dequeue())
                return self.cont2.dequeue()
        else:
            if self.cont1.size() == 1:
                return self.cont1.dequeue()
            else:
                while self.cont1.size() > 1:
                    self.cont2.enqueue(self.cont1.dequeue())

                return self.cont1.dequeue()

        

    def top(self) -> int:
        if self.cont2.is_empty() == self.cont1.is_empty() == True:
            return False
        elif self.cont1.is_empty() == True:
            if self.cont2.size() == 1:
                return self.cont2.peek()
            else:
                while self.cont2.size() > 1:
                    self.cont1.enqueue(self.cont2.dequeue())
                y =  self.cont2.peek()
                self.cont1.enqueue(self.cont2.dequeue())
                return y
        else:
            if self.cont1.size() == 1:
                return self.cont1.peek()
            else:
                while self.cont1.size() > 1:
                    self.cont2.enqueue(self.cont1.dequeue())

                y = self.cont1.peek()
                self.cont2.enqueue(self.cont1.dequeue())
                return y
        
        

    def empty(self) -> bool:
        return self.cont2.is_empty() == self.cont1.is_empty() == True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()