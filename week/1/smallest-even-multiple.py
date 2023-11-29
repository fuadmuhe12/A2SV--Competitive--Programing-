class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        start = n//1
        while True:
            if n%2 == 0:
                return n
            else:
                n += start