class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row  = len(matrix)
        col = len(matrix[0])
        ans = []
        start = 0
        while start < col:
            a = []
            for i in range(row):
                
                a.append(matrix[i][start])
            ans.append(a)
            start += 1
        return ans
