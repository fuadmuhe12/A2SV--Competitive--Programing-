class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>=0:
            x= list(str(num))
            x.sort()
            l = 0
            r = 0
            while r < len(x):
                if x[r] == "0":
                    r += 1
                    continue
                else:
                    x[l], x[r] = x[r], x[l]
                    break
            return int("".join(x))
        else:
            x= list(str(num)[1:])
            x.sort(reverse=True)
            
            return -int("".join(x))
            