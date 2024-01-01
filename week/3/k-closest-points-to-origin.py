class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for x, y in points:
            ans.append((x**2+y**2)**(1/2))
        dic_vals = defaultdict(list)
        for i in range(len(ans)):
            dic_vals[ans[i]].append(points[i])
        ans = sorted(dic_vals.keys())
        lst = []
        count =0 
        start = 0
        while count < k :
            for i in dic_vals[ans[start]]:
                lst.append(i)
                count += 1
                if count >= k:
                    break
            start += 1
        return lst
            