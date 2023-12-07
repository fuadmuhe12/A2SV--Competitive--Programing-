class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        dic_lose = defaultdict(int)
        all_team = set()
        for win ,los in matches:
            all_team.add(win)
            all_team.add(los)
            dic_lose[los] += 1
        return  [sorted([i for i in all_team if i not in dic_lose]), sorted([i for i in all_team if dic_lose[i] == 1])]
        