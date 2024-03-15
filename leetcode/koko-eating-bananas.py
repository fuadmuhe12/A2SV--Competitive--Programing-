class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =  1
        high =  max(piles)
        k = high
        while high >= low:
            pos_k = (low + high)//2
            need_h = 0
            for i in piles:
                need_h += math.ceil(i/pos_k)
            if need_h <= h:
                k = pos_k
                high = pos_k -1
            else:
                low = pos_k+1
        return k
            
            