class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        que =  deque()
        if len(deck) == 1:
            return deck
        que.append(deck.pop())
        while deck:
            bottom = que.pop()
            top =  deck.pop()
            que.appendleft(bottom)
            que.appendleft(top)
        return list(que)


