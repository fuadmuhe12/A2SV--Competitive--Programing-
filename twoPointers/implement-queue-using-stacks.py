class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


class MyQueue:

    def __init__(self):
        self.l1 = Stack()
        self.l2 = Stack()

    def push(self, x: int) -> None:
        if self.l1.is_empty() or self.l2.is_empty():
            self.l1.push(x)
        elif not self.l1.is_empty():
            self.l1.push(x)
        else:
            self.l2.push(x)




    def pop(self) -> int:
        if self.l1.is_empty() and self.l2.is_empty():
            return False
        elif not self.l1.is_empty():
            while self.l1.size() >1:
                self.l2.push(self.l1.pop())
            r= self.l1.pop()
            while self.l2.size() >0:
                self.l1.push(self.l2.pop())
            
            return r
        else:
            while self.l2.size() >1:
                self.l1.push(self.l2.pop())
            r= self.l2.pop()
            while self.l1.size() >0:
                self.l2.push(self.l1.pop())
            
            return r
        
            

    def peek(self) -> int:
        if self.l1.is_empty() and self.l2.is_empty():
            return False
        elif not self.l1.is_empty():
            while self.l1.size() > 1:
                self.l2.push(self.l1.pop())
            r = self.l1.peek()
            while self.l2.size() > 0:
                self.l1.push(self.l2.pop())

            return r
        else:
            while self.l2.size() > 1:
                self.l1.push(self.l2.pop())
            r = self.l2.peek()
            while self.l1.size() > 0:
                self.l2.push(self.l1.pop())

            return r

    def empty(self) -> bool:
        if self.l1.is_empty() and self.l2.is_empty():
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()