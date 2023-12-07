class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        for i in range(len(list1)) :
            if list1[i] in list2:
                ans.append((list2.index(list1[i]) + i ,list1[i] ))
        if len(ans) < 1:
            return []
        else:
            ans.sort()
            v= ans[0][0]
            return [j[1] for j in ans if j[0] == v]