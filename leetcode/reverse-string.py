class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rec(start, end, s):
            if start >= end:
                return 
            else:
                s[start], s[end] = s[end], s[start]
                rec(start + 1, end - 1, s)
        rec(0, len(s)-1, s)

        