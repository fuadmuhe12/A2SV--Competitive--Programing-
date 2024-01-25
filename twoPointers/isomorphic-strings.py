class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        t_s = {}
        s_t = {}
        ind  = 0
        while ind < len(s):
            if s[ind] in s_t and t[ind] != s_t[s[ind]] :
                return False
            else:
                s_t[s[ind]] = t[ind]
            
            if t[ind] in t_s and s[ind] != t_s[t[ind]]:
                return False
            else:
                t_s[t[ind]] = s[ind]
            ind += 1
        return True


 