# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        _len = len(board)
        widt = len(board[0])

        bor = set()
        seen = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (
                0 <= r < _len
                and 0 <= c < widt
                and board[r][c] == "O"
                and (r, c) not in seen
            ):
                seen.add((r, c))
                for i, j in dirs:
                    dfs(r + i, c + j)

        for i in range(_len):
            bor.add((i, 0))
            bor.add((i, widt - 1))

        for j in range(widt):
            bor.add((0, j))
            bor.add((_len - 1, j))

        for r, c in bor:
            dfs(r, c)

        for i in range(1, _len):
            for j in range(1, widt):
                if (i, j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"