class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        start = 0
        end = len(cardPoints)-k-1
        tot = sum(cardPoints)
        cur = sum(cardPoints[start: end+1])
        ans = tot - cur
        end += 1
        start
        while end < len(cardPoints):
            cur -= cardPoints[start]
            cur += cardPoints[end]
            ans= max(ans, tot-cur)
            end += 1
            start += 1
        return ans



