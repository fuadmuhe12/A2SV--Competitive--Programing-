class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        state = 1
        rows = len(mat)
        cols = len(mat[0])
        row = 0
        col = 0
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        ans = []
        while len(ans) < rows *cols:
            ans.append(mat[row][col])
            if state == 1:
                if 0 <= row-1 < rows and 0 <= col+1 < cols:
                    row -= 1
                    col += 1
                else:
                    if  0 <= row < rows and 0 <= col+1 < cols:
                        col += 1
                        
                    else:
                        row += 1
                    state = 0

            else:
                if  0 <= row+1 < rows and 0 <= col-1 < cols:
                    row += 1
                    col -= 1
                else:
                    if  0 <= row+1 < rows and 0 <= col < cols:
                        row += 1
                    else:
                        col += 1
                    state = 1
        return ans
