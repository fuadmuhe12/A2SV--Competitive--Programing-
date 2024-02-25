class Solution :
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        #u_s
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
            matrix[i] = [0] + matrix[i]
        ans = 0
        d = defaultdict(int)
        for c1 in range(n):
            for c2 in range(c1+1, n+1):
                t = 0
                d[0] = 1
                for r in range(m):
                    t += matrix[r][c2] - matrix[r][c1]
                    if(t - target in d):
                        ans += d[t - target]
                    d[t] += 1
                d.clear()
        return ans