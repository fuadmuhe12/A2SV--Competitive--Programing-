class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        num_version = []
        for j in words:
            cur = []
            for x in j:
                cur.append(dic[x])
            num_version.append(cur)
        return num_version == sorted(num_version)
