# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        df = defaultdict(list)

        for j in strs:
            s = defaultdict(int)
            for i in j:
                s[i] += 1
            df[tuple(sorted(s.items()))].append(j)
        return df.values()


