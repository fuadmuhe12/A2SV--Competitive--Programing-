class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dire = [(-1,0), (1,0), (0,-1), (0,1)]
        guarded = set()
        gset = set(tuple(g) for g in guards)
        wset = set(tuple(w) for w in walls)
        for gx, gy in guards:
            for dx, dy in dire:
                x = gx
                y = gy
                while (0 <= dx + x < m) and (0 <= dy + y < n) and (tuple([x+dx, y+dy]) not in wset) and (tuple([x+dx, y+dy]) not in gset):
                    guarded.add(tuple([x+dx, y+dy]))
                    x += dx
                    y += dy
        
        return m*n - len(gset) - len(wset) - len(guarded)