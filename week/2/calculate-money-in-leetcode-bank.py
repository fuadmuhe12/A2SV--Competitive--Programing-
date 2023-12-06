class Solution:
    def totalMoney(self, n: int) -> int:
        tot = 1
        mon = 1
        start = 1
        cur = 1
        for start in range(1, n):
            if start %7 == 0:
                mon += 1
                tot += mon
                cur = mon 
                start +=1
                continue
            else:
                cur += 1
                tot += cur
            start += 1
        return tot



