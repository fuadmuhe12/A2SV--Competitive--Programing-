class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [i for i in s]
        t = [i for i in t]
        if len(s) != len(t):
            return False
        ind = 0
        while ind < len(s):
            if s[ind] not in t:
                return False
            t.remove(s[ind])
            ind += 1
        return True
