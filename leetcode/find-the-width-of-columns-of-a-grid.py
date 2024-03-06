class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        start = 0 
        ans = []
        for start in range(0, len(grid[0])):
            mx = 0
            for i in grid:
                if start == len(grid[0]):
                    break
                mx =  max(mx, len(str(i[start])))
            ans.append(mx)
        return ans

            


        