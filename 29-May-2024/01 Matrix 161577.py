# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        visited = [[float('inf')] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    visited[i][j] = 0
                    queue.append((i,j))
                    
        while queue: 
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if visited[new_row][new_col] > visited[row][col] + 1:
                            visited[new_row][new_col] = visited[row][col] + 1
                            queue.append((new_row, new_col))
        return visited