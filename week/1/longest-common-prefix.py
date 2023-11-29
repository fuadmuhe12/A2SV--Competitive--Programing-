class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = 0
        ans = ""
        mn = min([len(i) for i in strs] )
        while start < mn:
            cur = strs[0][start]
            for i in strs:
                if i[start] == cur:
                    pass
                else:
                    return ans
            
            ans += cur
            start += 1
        return ans