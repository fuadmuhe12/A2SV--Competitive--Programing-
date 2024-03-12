class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        for ind, val in enumerate(order):
            dic[val] = ind
        return ''.join(sorted(list(s), key = lambda a: -1 if a not in dic else dic[a] ))
