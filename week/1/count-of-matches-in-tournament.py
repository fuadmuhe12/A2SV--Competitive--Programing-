class Solution:
    def numberOfMatches(self, n: int) -> int:
        mach =0
        team = n
        while n > 1:

            if n% 2 == 0:
                mach += n//2
                n = n//2
            else:
                mach += (n-1)//2
                n =(n-1)//2 + 1
        return mach
