class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        mx = 0
        for i in range(1, len(points)):
            mx = max((points[i][0] - points[i-1][0]), mx)
        return mx