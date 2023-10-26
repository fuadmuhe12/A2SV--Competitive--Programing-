class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches = 0
        available_trainers = trainers.copy()

        for player in players:
            for i, trainer in enumerate(available_trainers):
                if player <= trainer:
                    matches += 1
                    available_trainers.pop(i)
                    break

        return matches

