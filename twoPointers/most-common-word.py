class Solution:
    import re
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bad =  set(banned)
        # bad.add(list("! ? ' , ; .".split()))
        val = sorted(Counter(list(re.split(r'[!?\',;. ]', paragraph.lower()))).items(), key = lambda x : x[1], reverse = True)
        print(val)
        for v, rep in val :
            if  v not in bad and v != "":
                return v