class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # result = list(s)
        # start = 0
        # for i in spaces:
        #     result.insert( i+ start, ' ')
        #     start += 1
        # final = ""
        # for i in result:
        #     final += i
        
        res = ""
        start = 0
        inc = 0 # incrementing value
        for end in spaces:
            res += s[start: end]
            res += " "
            start = end 
        res += s[start:]
    

        return res
