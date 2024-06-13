# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(1, len(memo)):
            for c in range(1, len(memo[0])):
                if matrix[r - 1][c - 1] == '1':
                    memo[r][c] = min(memo[r - 1][c], memo[r][c - 1], memo[r - 1][c - 1]) + 1
        return max(c for r in memo for c in r) ** 2  