# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for i in range(n)]
        for val in range(2, n):
            for i in range(n - val):
                j = i + val
                dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[j] * values[k] for k in range(i + 1, j))
        return dp[0][n - 1]