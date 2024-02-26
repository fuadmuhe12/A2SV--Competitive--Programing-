class Solution:
    def splitString(self, s: str) -> bool:
            
                
        def rec(s,st, i, agg):
            if i >= len(s):
                return True if agg != int(s)-1 else False
            else:
                for j in range(st, len(s)):
                    cur  =   int(s[st:j+1])
                    if cur == agg:
                        if rec(s,j+1, j+1,agg-1):
                            return True
                return False
        for i in range(1, len(s)+1):
                agg = int(s[:i])
                nex =  rec(s,i, i, agg-1)
                if nex:
                    return True
        else:
            return False    
        
                        



                    






