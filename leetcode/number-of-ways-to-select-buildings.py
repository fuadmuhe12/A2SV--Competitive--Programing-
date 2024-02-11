class Solution:
    def numberOfWays(self, s: str) -> int:
        zer = s.count("0")
        one = len(s) -zer
        lz = 0 if s[0] == "1" else 1
        lo = 0 if s[0] == '0' else 1
        rz = zer - lz
        ro = one - lo
        ans = 0
        for i in range(1, len(s)):
            if s[i] == "1":
                ans += lz*rz
                lo += 1
                ro -= 1
            else:
                ans += ro*lo
                rz -= 1
                lz += 1
        return ans

