# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0
        
        m, n = len(dungeon), len(dungeon[0])
        
        # Initialize the dp array with infinity
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: knight needs at least 1 health point to survive
        dp[m][n-1] = dp[m-1][n] = 1
        
        # Bottom-up calculation
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0][0]
