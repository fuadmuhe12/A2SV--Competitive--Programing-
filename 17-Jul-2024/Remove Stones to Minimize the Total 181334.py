# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-x for x in piles]
        heapify(maxHeap)

        for i in range(k):
            val = heappop(maxHeap)
            heappush(maxHeap, val - int(val / 2))
        return -1 * sum(maxHeap)