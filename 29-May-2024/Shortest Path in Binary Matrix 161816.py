# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        len_ = len(grid)

        if grid[0][0] != 0 or grid[len_ - 1][len_ - 1] != 0:
            return -1

        dirs = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        queue = deque([(0, 0, 1)]) 


        while queue:

            row, col, curLen = queue.popleft()

            if row == len_ - 1 and col == len_ - 1:
                return curLen

            for i, j in dirs:
                neighbour_row = i + row
                neighbour_col = j + col

                if (
                    0 <= neighbour_row < len_
                    and 0 <= neighbour_col < len_
                    and grid[neighbour_row][neighbour_col] == 0
                ):
                    grid[neighbour_row][neighbour_col] = 1
                    queue.append((neighbour_row, neighbour_col, curLen + 1))

        return -1
