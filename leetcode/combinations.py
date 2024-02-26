class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        used  =  dict()
        def rec(n, m, temp=[]):
            nonlocal k
            if m > k:
                ans.append(temp[:])
                del used[temp.pop()] 
                return 
            for i in range(temp[-1] if temp else 1
, n+1):
                if i  in used:
                    continue
                temp.append(i)
                used[i] = 1
                rec(n, m+1, temp)
            if temp:
                del used[temp.pop()]
        rec(n, 1)
        return ans
        

            



            