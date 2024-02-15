class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        odd = True
        for i in count.values():
            if i % 2 and odd:
                ans += 1
                odd = False
            if i % 2:
                ans += i-1
            else:
                ans += i
            

        return ans