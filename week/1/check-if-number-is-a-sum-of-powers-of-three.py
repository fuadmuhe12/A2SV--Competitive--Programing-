class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 1
        sums = 0
        visited  = set()
        while True:
            if x + sums == n and x not in visited:
                return True
            elif x + sums > n:
                if x//3 not in  visited: 
                    sums += x//3
                    visited.add(x//3)
                    x = 1
                else:
                    return False 
                if sums > n:
                    return False
                continue
            elif sums == n:
                return True
            elif sums > n:
                return False
            x *= 3
            
            

        