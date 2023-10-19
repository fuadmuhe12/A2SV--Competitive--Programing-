from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start = 0
        end = len(skill) - 1
        re = 0
        tot = skill[start] + skill[end]
        while start < end:
            if skill[start] + skill[end] != tot:
                return -1
            re += skill[start] * skill[end]
            start += 1
            end -= 1

        return re
