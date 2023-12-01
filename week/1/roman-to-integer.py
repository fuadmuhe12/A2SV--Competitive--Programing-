class Solution:
    def romanToInt(self, s: str) -> int:
        sums = 0 
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        start = 0
        while start < len(s):
            if start + 1 < len(s) and dic[s[start]] > dic[s[start + 1]]:
                sums += dic[s[start]]
                start += 1
            elif start + 1 < len(s) and dic[s[start]] < dic[s[start + 1]]:
                sums += dic[s[start +1]] - dic[s[start]]
                start += 2
            else :
                sums += dic[s[start]]
                start += 1
        return sums
        