class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        '''
        [['(', 3], [')', 1]], [['(', 3], [')', 2]]
        '''
        def rec(opn ,close,  temp):
            if  opn == n and close == n:
                ans.append(temp[:])
                return 
            
            for i  in range(1, n - opn + 1):
                opn += i
                for clo  in range(1, opn-close +  1):
                    close += clo
                    temp.append(['(', i])
                    temp.append([')', clo])

                    rec(opn , close,  temp )
                    temp.pop()
                    temp.pop()
                    close -= clo
                opn -= i
        rec(0,  0, [])
        final = []
        for i in ans:
            sub = []
            for x, y in i:
                sub.extend([x] *y)
            final.append("".join(sub))
            



        return final

            










