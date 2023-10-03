class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        # def DFS(node, h):
        #     visited.add(node)
        #     for i in graph[node]:
        #         h.append(i)
        #         DFS(i, h)
            
        #     return h
        # dics = {}
        # for i in nodes:
        #     if i not in visited:
        #         for j in nodes:
        #             if i not in graph[j]:
        #                 dics[i] = DFS(i, [])
        # keys = list(dics.keys())
        
        # for j in keys:
        #     for m in keys:
        #         if m != j and j in graph[m]:
        #             del dics[j]
        # return list(dics.keys())

        incoming= {}
        for s, e in edges:
            incoming[e] = None
        answer = [nm for nm in range(n) if nm not in incoming]
       
        return answer
            

            
        
