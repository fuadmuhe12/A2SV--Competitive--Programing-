# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind2:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

    def Find(self, x): 
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]    

    def Union(self, x, y):
        xRoot = self.Find(x)
        yRoot = self.Find(y)
        #do rank here- 
        if xRoot == yRoot:
            return False
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = self.parent[yRoot]
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = self.parent[xRoot]
        else:
            self.parent[yRoot] = self.parent[xRoot]
            self.rank[xRoot] += 1
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind2(len(edges))
        for u, v in edges:
            if not uf.Union(u,v):
                return [u,v]