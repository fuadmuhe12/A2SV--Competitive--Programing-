# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >1:
            end1 = stones.pop()
            end2 = stones.pop()
            res = abs(end1-end2)
            if res >0:
                stones.append(res)
                stones.sort()
        return stones[0] if len(stones) >0 else  0