class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {'N':(0,1), 'E':(1,0),'W':(-1,0),'S':(0,-1)}
        vis = set()
        
        x = 0
        y = 0
        vis.add((x,y))
        for i in path:
            nx, ny  = dir[i]
            x += nx
            y += ny
            print(x,y)
            if (x, y) in vis:
                return True
            else:
                vis.add((x, y))
        else:
            return False

