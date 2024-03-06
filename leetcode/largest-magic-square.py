class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rpre = [[0] for i in range(len(grid))]
        for ind, row in enumerate(grid):
            acc = 0
            for col in row:
                acc += col
                rpre[ind].append(acc)

        cpre = [[0] for i in range(len(grid[0]))]

        for col in range(len(grid[0])):
            acc = 0
            for row in grid:
                acc += row[col]
                cpre[col].append(acc)
        def check(rs, cs, re, ce):
            if re - rs == 0:
                return True
            comp = rpre[rs][ce+1] - rpre[rs][cs]

            for rows in range(rs, re +1):
                cur = rpre[rows][ce+1] - rpre[rows][cs]
                if cur != comp:
                    return False
            for cols in range(cs, ce +1):
                cur = cpre[cols][re+1] - cpre[cols][rs]
                if cur != comp:
                    return False
            disum = 0
            negsum = 0
            nrs = rs
            ncs = ce
            for i in range(re-rs+1):
                disum += grid[rs][cs]
                negsum += grid[nrs][ncs]
                rs += 1
                cs += 1
                nrs += 1
                ncs -= 1
            if comp != disum or comp != negsum:
                return False
            return True
        rlen =  len(grid[0])
        clen = len(grid)
        mx = 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                for end in range(1, min(rlen- col, clen - row)):
                    ce = col + end
                    re =  row + end
                    if check(row, col, re, ce):
                        mx = max(mx , re - row +1)
        return mx




                



