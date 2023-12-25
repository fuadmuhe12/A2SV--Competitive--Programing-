class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        row = 0
        col = 0
        r = n-1
        sun = 0
        while 0 <= row < n and 0 <= col < n and 0 <= r < n:
            sun += mat [row][col] + mat[r][col]
            row += 1
            col += 1
            r -= 1
        if n%2:
            sun -= mat[(n)//2][(n)//2]
        return sun
            


