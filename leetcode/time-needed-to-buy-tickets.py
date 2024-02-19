class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        m = tickets[k]
        t = 0
        front = tickets[:k+1]
        back = tickets[k+1:]
        total = 0
        for i in front:
            total += min(i, m)
        if m >= 2:
            for i in back:
                total += min(i, m-1)
        return total
