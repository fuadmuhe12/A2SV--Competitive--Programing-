class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        bigger  = []
        smaller = []
        for i in range(1,n+1 ):
            if n %i == 0 :
                if bigger and  i == bigger[-1]:
                    break
                smaller.append(i)
                if n//i != i:
                    bigger.append(n//i)
        smaller += bigger[::-1]
        print(smaller)
        if k <= len(smaller):
            return smaller[k-1]
        else:
            return -1