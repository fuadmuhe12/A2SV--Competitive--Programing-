class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    value = int(board[i][j])
                    row[i].add(value)
                    col[j].add(value)
# simple arithmetic formula to get the current block id
                    cur_id = i//3 * 3 + j//3
                    square[cur_id].add(value)
                    
        def backtrack(i, j):
            nonlocal ans 
            if i == 9:
                ans = True
                return
            i1 = i+(j+1)//9
            j1 = (j+1)%9
            if board[i][j] != ".":
                backtrack(i1, j1)
            else:
                for num in range(1, 10):
# reusing the same current block formula
                    cur_id = i//3 * 3 + j//3
                    if num not in row[i] and num not in col[j] and num not in square[cur_id]:
                        row[i].add(num)
                        col[j].add(num)
                        square[cur_id].add(num)
                        board[i][j] = str(num)
                        backtrack(i1, j1)
                        if ans == False:
                            row[i].remove(num)
                            col[j].remove(num)
                            square[cur_id].remove(num)
                            board[i][j] = '.'
        ans = False
        backtrack(0, 0)