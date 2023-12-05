class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_length = abs(target[0]) + abs(target[1])
        gost_length = [ abs(x-target[0]) +abs( y-target[1] )   for x, y in ghosts ]
        return my_length < min(gost_length )