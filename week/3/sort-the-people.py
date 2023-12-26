class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        #slectection sort
        s = 0
        while s < len(n):
            l = s+ 1
            while l < len(n):
                if h[l] > h[s]:
                    h[l], h[s] = h[s], h[l]
                    n[l], n[s] = n[s], n[l]

                l += 1
            s+= 1
        return n
        




                

 