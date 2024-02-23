class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for ind, val in enumerate(s):
            if val not in dic:
                dic[val] = [ind, ind]
            else:
                dic[val][1] = ind
        end =None
        start = 0
        ans = []
        for ind, val in enumerate(s):
            if end == None:
                end = dic[val][1]
            else:
                end = max(end, dic[val][1])
            if end ==  ind:
                ans.append(end -start +1)  
                start = end +1  
                end =  None 
        return ans

