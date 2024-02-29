class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows =  len(board)
        cols=  len(board[0])
        dir = [(-1,0), (1, 0), (0, -1), (0, 1)]
        def isbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        starts = []
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    starts.append([row, col])
                
        if len(word) == 1:
            return True if starts else False
        def backtrack(row, col, seen, ind):
            if ind >= len(word):
                return True
            
            if board[row][col] != word[ind]:
                
                return 
            if ind == len(word)-1:
                return True
            for r, c in dir:
                nr = row +r
                nc = col + c
                if isbound(nr, nc) and (nr, nc) not in seen :
                    seen.add((nr, nc))
                    if backtrack(nr, nc, seen, ind + 1):
                        return True
                    seen.remove((nr, nc))
            
        for  row , col in starts:
            seen = set()
            seen.add((row, col))
            if backtrack(row, col, seen ,0):
                return True
            seen.remove((row, col))
        return False



