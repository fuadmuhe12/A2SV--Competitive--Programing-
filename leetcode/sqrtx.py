class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        mid = (start + end)// 2
        if x== 1:
            return 1
        while True:
            if mid *mid > x:
                end = mid
                mid = (start + end)//2
            elif mid * mid == x :
                return mid
            elif end- start == 1:
                return start
            else:
                start = mid 
                mid  = (start + end)//2
        




        