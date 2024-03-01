class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        import copy
        ans = []
        def backtrack(pos, r ,negDia, posDia, usedCol):
            if len(pos) == n:
                ans.append(pos[:])
                return 

            for col in range(n):
                if col not in usedCol and  r-col not in negDia and r+ col not in posDia:

                    pos.append((r, col))
                    negDia.add(r-col)
                    posDia.add(r+col)
                    usedCol.add(col)

                    backtrack(pos, r+1, negDia, posDia, usedCol)

                    pos.pop()
                    negDia.remove(r-col)
                    posDia.remove(r+col)
                    usedCol.remove(col)
        

        backtrack([], 0, set(), set(), set())
        final = []
        for ind, pos in enumerate(ans):
            chess = [["." for i in range(n)] for i in range(n)]
            for i in range(n):
                row, col =  pos[i]
                chess[row][col]= ("Q") 
            for i in  range(n):
                chess[i] = "".join(chess[i])
            final.append(deepcopy(chess))
        return final
                    