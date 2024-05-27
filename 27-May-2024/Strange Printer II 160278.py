# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

from collections import defaultdict

class Solution:
    def isPrintable(self, targetGrid):
        rows, cols = len(targetGrid), len(targetGrid[0])
        dependencies = defaultdict(set)

        for color in range(1, 61):
            row_min = col_min = 60
            row_max = col_max = 0

            for row in range(rows):
                for col in range(cols):
                    if targetGrid[row][col] == color:
                        row_min = min(row_min, row)
                        row_max = max(row_max, row)
                        col_min = min(col_min, col)
                        col_max = max(col_max, col)

            for row in range(row_min, row_max + 1):
                for col in range(col_min, col_max + 1):
                    if targetGrid[row][col] != color:
                        dependencies[color].add(targetGrid[row][col])

        def hasCycle(color):
            if visited[color]: 
                return visited[color] == 1
            visited[color] = 1
            if any(hasCycle(dep) for dep in dependencies[color]): 
                return True
            visited[color] = 2
            return False 

        visited = [0] * 61

        return not any(hasCycle(color) for color in range(1, 61))
