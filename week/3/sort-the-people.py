class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        dic = defaultdict(list)
        ans = []
        for i in range(len(n)):
            dic[h[i]].append(n[i])
        for i in sorted(dic.keys(), reverse =True):
            ans.extend(dic[i])
        return  ans



                

 