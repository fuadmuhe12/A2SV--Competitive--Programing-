class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = [[] for i in range(len(matrix))]
        for i in range(len(matrix)-1, -1, -1):
            for cols in range(len(matrix)):
                ans[cols].append(matrix[i][cols])
        for i in range(len(ans)):
            matrix[i] = ans [i]

            
       