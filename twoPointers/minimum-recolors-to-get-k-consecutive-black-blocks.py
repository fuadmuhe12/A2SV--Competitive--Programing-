class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        how to appraoch : we use window static with length of k  and
        calculating the max value of the black in the vindow then 
        just mx - k 

        what do we need: two pointer(start=0 ,end=0) Black =0 counter
        '''
        start = 0
        end = 0
        bla = 0
        mx = 0
        while end < k :
            if blocks[end] == "B":
                bla += 1
            end += 1
        mx = max (mx, bla)

        while end < len(blocks):
            if blocks[start] == "B":
                bla -= 1
            if blocks[end] == "B":
                bla += 1
            mx = max( mx, bla)
            start += 1
            end += 1
        return  k-mx

                 

