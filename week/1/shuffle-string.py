class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        for i in range(len(indices)):
            s[i] = [s[i], indices[i]]
        s.sort(key = lambda x: x[1])
        ans = ''
        for i in s:
            ans += i[0]
        return ans