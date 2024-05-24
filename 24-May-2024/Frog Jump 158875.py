# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: list[int]) -> bool:
        set_st = set(stones)

        @cache
        def posJump(index, k):
            return index == stones[-1] or any(
                x and x + index in set_st and posJump(index + x, x)
                for x in range(k - 1, k + 2)
            )
        
        return posJump(stones[0], 0)
