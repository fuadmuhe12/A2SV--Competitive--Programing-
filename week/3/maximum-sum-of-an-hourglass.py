class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def val(row, col):
            return grid[row][col]+grid[row+2][col]+grid[row][col+1]+grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col+1]+grid[row+2][col+2]
        rows = len(grid)
        cols = len(grid[0])
        ans = []
        for row in range(0, rows-3+1):
            for col in range(0, cols-3+1):
                ans.append(val(row, col))
        return max(ans)
