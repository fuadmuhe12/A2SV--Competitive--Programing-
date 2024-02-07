class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_mat =  [[ 0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                left =[row, col-1]
                top  = [row -1, col]
                dia = [row -1, col-1]
                if 0 <= top[0] < len(matrix) and 0 <= left[1] < len(matrix[0]):
                    self.prefix_mat[row][col] =   self.prefix_mat[top[0]][top[1]] + self.prefix_mat[left[0]][left[1]] - self.prefix_mat[dia[0]][dia[1]] + matrix[row][col]
                elif 0 <= top[0] < len(matrix):
                    self.prefix_mat[row][col] = self.prefix_mat[top[0]][top[1]] + matrix[row][col]
                elif 0 <= left[1] < len(matrix[0]):
                    self.prefix_mat[row][col] = self.prefix_mat[left[0]][left[1]] + matrix[row][col]
                else:
                    self.prefix_mat[row][col] =  matrix[row][col]
        
        print(matrix, "matrix")
        print(self.prefix_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        bot = [row2, col2]
        top = [row1 -1, col2]
        left = [row2, col1-1]
        dia = [row1-1, col1-1]
        if 0 <= top[0] < len(self.matrix) and 0 <= left[1] <len(self.matrix[0]):
            ans = self.prefix_mat[row2][col2] - self.prefix_mat[left[0]][left[1]] - self.prefix_mat[ top[0] ]  [top[1] ] + self.prefix_mat[ dia[0] ] [ dia[1] ]
        elif 0 <= top[0] < len(self.matrix):
            ans = self.prefix_mat[row2][col2]- self.prefix_mat[top[0] ][top[1]] 
        elif  0 <= left[1] < len(self.matrix[0]):
            ans = self.prefix_mat[row2][col2] - self.prefix_mat [left[0]]  [left[1] ] 
        else:
            ans = self.prefix_mat[row2][col2]
        return ans
           







# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)