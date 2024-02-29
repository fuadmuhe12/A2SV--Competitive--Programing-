class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        mr = [max(i) for i in grid]
        mc = []
        col , row = 0, 0
        while col < len(grid[0]):
            row = 0
            mx =  grid[row] [col]
            while row < len(grid):
                mx = max(grid[row][col], mx)
                row += 1
            mc.append(mx)
            col += 1

        fin = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                mn = min(mc[col], mr[row])
                if grid[row] [col] < mn:
                    fin +=  mn - grid[row] [col] 
        return fin

