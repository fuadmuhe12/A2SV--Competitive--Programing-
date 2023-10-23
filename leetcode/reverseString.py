
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rec(m,n):
            if m >= n:
                return
            s[n], s[m] = s[m], s[n]
            rec(m+1, n-1)
        rec(0,len(s)-1)

    


        
