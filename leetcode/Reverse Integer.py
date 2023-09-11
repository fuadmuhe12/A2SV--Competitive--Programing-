class Solution:
    def reverse(self, x: int) -> int:
        def revToBit(num):
            store = []
            if num < 0:
                while num < 0:
                    store.append(-(num % 2))
                    num = math.ceil(num / 2)
                return store
            else:
                while num > 0:
                    store.append(num % 2)
                    num = math.floor(num / 2)
                return store
        def rev(num):
            *st, = str(num)
            x = st[::-1]
            last = ''
            q = False
            for i in x:
                if i != '-':
                    last += i
                else:
                    q = True
                    
            val =int(last)
            if q:
                val = -val
            return val
        y = rev(x)
        if -2**31 <= y <= 2**31 -1 :
            return y
        else:
            return 0
            
