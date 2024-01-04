from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alf = "qwertyuioplkjhgfdsazxcvbnm"
        
        alph = defaultdict(int)

        for j in alf:
            alph[j] = 0
        comp = defaultdict(int)
        for j in alf:
            comp[j] = 0
        for i in p:
            alph[i] += 1
        start = 0 
        end = 0
        ans = []
        if len(p) > len(s):
            return []
        else:
            while end < len(s):
                comp[s[end]] += 1
                if end < len(p)-1:
                    end += 1
                else:
                    if comp == alph:
                        ans.append(start)
                        comp[s[start]] -= 1
                        end += 1
                        start +=1
                    else:
                        comp[s[start]] -= 1
                        end += 1
                        start += 1

        return ans                        




        