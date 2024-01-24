class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        cur_start = 0
        ans = []
        for ind, val in enumerate(firstList):
            x, y = val
            if cur_start >= len(secondList):
                break
            change = False
            sec = cur_start
            while cur_start < len(secondList) and sec < len(secondList):
                a, b = secondList[sec]
                if y >=  a and x <= b:
                    ans.append([max(x, a), min(y, b)])
                    change = True
                elif change :
                    break
                if not change and x > b : #after opartion 
                    cur_start += 1
                sec += 1
        return ans




