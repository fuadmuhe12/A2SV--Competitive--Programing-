class RecentCounter:

    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        self.stack.append(t)
        if t< 3000:
            return len(self.stack)
        

        def finds(t):
            start  = 0
            look = t -3000
            end  = (len(self.stack))-1
            
            while  start < end:
                mid = (end + start)//2
                if self.stack[mid] > look:
                    end = mid
                elif  self.stack[mid] < look:
                    start = mid + 1
                else:
                    return mid
            if self.stack[end] < look:
                return end + 1
            else:
                return end
        return len(self.stack[finds(t):])
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)