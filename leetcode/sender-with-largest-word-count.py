class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        curmax = float('-inf')
        name = ''
        dic = defaultdict(int)

        for ind, val in enumerate(messages):
            cur = len(list(val.split(' '))) 
            dic[senders[ind]] += cur

        for i in dic.keys():
            if dic[i] >= curmax:
                name = i if curmax < dic[i] else max(name,i)
                curmax = max(curmax, dic[i])
        return name
                

            
