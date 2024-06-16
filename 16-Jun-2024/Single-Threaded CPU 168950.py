# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ind = []
        for i in range(len(tasks)):
            ind.append([tasks[i][0],tasks[i][1],i])
        ind.sort(key=lambda x:x[0])
        req = []
        val = []
        cur = 0
        i = 0
        while (len(val)<len(tasks)):
            while i <len(ind) and ind[i][0]<=cur:
                heapq.heappush(req,(ind[i][1],ind[i][2]))
                i+=1
            if not req:
                cur = ind[i][0]
            else:
                s,curI = heapq.heappop(req)
                cur+=s
                val.append(curI)
        return val
                