class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p1= 0 
        p2 = 0
        while p2 < len(s) and p1 < len(g):
            if g[p1] <= s[p2]:
                p1 += 1
                p2 += 1
            else:
                p2+= 1
        return p1