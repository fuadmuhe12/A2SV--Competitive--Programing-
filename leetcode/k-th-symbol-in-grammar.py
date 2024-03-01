class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        path = deque()
        dic = {1: 0, 2:1, 3:1, 4: 0}
        def rec(k):
             
            path.appendleft(k)
            if k <=4:
                return
            if k%2:
                rec((k+1)//2 )
            else:
                rec(k//2)
        rec(k)
        def fin(ind, cur):
            if ind == len(path)-1:
                return cur
            if cur == 1:
                if path[ind + 1] % 2:
                    return fin(ind+1,1 )
                else:
                    return fin(ind+1,0)
            else:
                if path[ind + 1] % 2:
                    return fin(ind+1,0 )
                else:
                    return fin(ind+1,1)
        return ( fin(0, dic[path[0]]))




