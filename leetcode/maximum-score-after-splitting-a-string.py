class Solution:
    def maxScore(self, s: str) -> int:
        zer = 0
        one = 0
        for i in s:
            if i == "1":
                one += 1
            else:
                zer += 1
        cur_zer = 0
        mx = 0
        for ind in range(len(s)-1):
            if s[ind] == "0":
                cur_zer += 1
                
            else:
                one -= 1
            mx =  max(mx, cur_zer + one)
    
        return mx
