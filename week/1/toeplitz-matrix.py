class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # for i in range(len(matrix)):
        #     cur = matrix[i][i]
        #     for j in range(i, len(matrix[0])):
        #         if matrix[i][j] != cur:
        #             return False
        # return True
        x = 0
        y = len(matrix)-1

        while x < len(matrix[0]) and y >= 0:
            print(f"x= {x} y {y}")
            cur  = matrix[y][x]
            k = x//1
            m = y //1
            while k < len(matrix[0]) and m < len(matrix):
                if matrix[m][k] != cur:
                    return False
                m += 1
                k += 1
            if y>0:
                y-= 1
            else:
                x+=1
        return True


