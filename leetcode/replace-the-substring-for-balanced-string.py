
from collections import Counter,defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        #u_s
        unba = Counter(s) - Counter({a: len(s)//4 for a in 'QWER'})
        if not unba:
            return 0
        
        ans = len(s)
        inds = defaultdict(list)
        for i, a in enumerate(s):
            inds[a].append(i)
            if any(len(inds[k]) < v for k, v in unba.items()):
                continue
            ans = min(ans, i - min(inds[k][-v] for k, v in unba.items()) + 1)
        return ans