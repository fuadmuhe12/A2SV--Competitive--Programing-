# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        tot, final = 0, 0
        heap, pair = [], zip(efficiency, speed)

        pair = sorted(pair, key=lambda x: x[0], reverse=True)
        for val in pair:
            if len(heap) >= k:
                mi = heapq.heappop(heap)
                tot -= mi
            heapq.heappush(heap, val[1])
            tot += val[1]
            final = max(final, tot * val[0])
        return final % (10 ** 9 +7)