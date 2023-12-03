class Solution:
    def printVertically(self, s: str) -> List[str]:
        start = 0
        ans = []
        lst = list(s.split())
        ln = list(map(len, s.split()))
        while start < max(ln):
            ans.append("")
            for i in range(len(lst)):
                if ln[i] > start:
                    ans[start] += lst[i][start]
                else:
                    ans[start] += " "
            start += 1
        return [ i.rstrip() for i in ans]

                    


