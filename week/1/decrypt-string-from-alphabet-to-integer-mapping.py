class Solution:
    def freqAlphabets(self, s: str) -> str:
        alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        dic  = {}
        for i in range(len(alp)):
            cur = i + 1
            dic[cur] = alp[i]
        start = 0
        ans = ''
        while start < len(s):
            if start + 2 < len(s) and s[start + 2] == "#" :
                m = int(s[start:start +2])
                ans += dic[m]
                start += 3
            else:
                m =  int(s[start])
                ans += dic[m]
                start += 1
        return ans



