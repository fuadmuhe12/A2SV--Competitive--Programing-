class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        we gonna use prefix summ first creating empty arry of 0 with len og th equal to the 
        given array ,


        """
        ary = [0]*(n)
        for start, end, val in bookings:
            ary[start-1] += val
            if end-1 < n-1:
                ary[end] -= val
        prex = [0]*n
        acc = 0
        for ind, val in enumerate(ary):
            acc += val
            prex[ind] = acc
        return prex
            
            

