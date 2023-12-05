class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cur  = 0
        for i in range(1, len(points)):
            val = max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
            cur  += val
        return cur