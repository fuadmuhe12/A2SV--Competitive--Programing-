class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        dicfreq_row = {}
        dicfreq_colm = {key:0 for key in range(len(mat[0]))}

        for i in range(len(mat)):
            dicfreq_row[i]= mat[i].count(1)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    dicfreq_colm[col] += 1
        ans = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1 and dicfreq_row[row] == 1 and dicfreq_colm[col] == 1:
                    ans += 1
        return ans
        





        
            

