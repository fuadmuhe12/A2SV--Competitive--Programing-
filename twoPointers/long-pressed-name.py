class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # use two dynamic window one on the name  and one on the typed if the typed window has the 
        # has the same elmenets and greater or equal len then it's a pass
        #name
        start = 0
        end  = 0
        cur = name[start]
        #typed
        l = 0
        r = 0
        ty = typed[l]
        if len(typed) < len(name):
            return False
        else:
            while r < len(typed) and end < len(name):
                while end < len(name) and name[end] == cur :
                    end += 1
                while r < len(typed) and typed[r] == ty:
                    r += 1
                if cur != ty or r-l < end - start:
                    return False
                l = r 
                start = end
                if start < len(name): 
                    cur =  name[start]
                if  l < len(typed):       
                    ty = typed[l]
            
            return True if r == len(typed) and end == len(name) else False