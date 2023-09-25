vertex = int(input())
operation = int(input())
from collections import defaultdict
graph = defaultdict(list)

for i in range(operation):
    line = list(map(int, input().split()))

    if line[0] == 1:
        graph[line[1]].append(line[2])
        graph[line[2]].append(line[1])
    else:
        x = list(graph[line[1]])
        for neighbor in x:
            print(neighbor, end=' ')
