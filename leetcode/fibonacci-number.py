class Solution:
    def fib(self, n: int) -> int:
        dic = {0 : 0, 1: 1}
        def rec(n):
            if n in dic:
                return dic[n]
            one = rec(n-1)
            dic[n] = dic[n - 1] + dic[n - 2]
            two = dic[n - 2]
            return one + two
        return rec(n)
            