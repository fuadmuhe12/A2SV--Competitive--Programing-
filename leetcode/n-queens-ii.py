class Solution:
    def totalNQueens(self, n: int) -> int:
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
        return len(ans)
                    