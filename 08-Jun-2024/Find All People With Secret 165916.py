# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = {}
        for person1, person2, time in meetings:
            if time not in graph:
                graph[time] = defaultdict(list)    
            graph[time][person1].append(person2)
            graph[time][person2].append(person1)

        perSecret = {0, firstPerson}
        for time in sorted(graph.keys()):
            val = graph.pop(time)

            perShareSec = set(person for person in val.keys() if person in perSecret)
            while perShareSec:
                perRecSec = set()
                for person in perShareSec:
                    perRecSec.update(person for person in val[person] if person not in perSecret)

                perShareSec = perRecSec
                perSecret.update(perShareSec)
        return list(perSecret)