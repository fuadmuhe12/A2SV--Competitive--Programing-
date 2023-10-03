class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # converting adjecency list and then counting the numer of neighbour iwth hight being the center 
        # from collections import defaultdict
        # graph = defaultdict(list)
        # for m , n in edges:
        #     graph[m].append(n)
        #     graph[n].append(m)
        # maxs = len(graph[1])
        # answer = 1
        # for j in range(1, len(edges)+2):
        #     if len(graph[j]) > maxs:
        #         maxs = len(graph[j])
        #         answer = j
        # return answer


        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
