class Solution:
    def bestClosingTime(self, customers: str) -> int:
        dic = {0:0}
      
        acc = 0
        for ind, val in enumerate(customers):
            acc += 1 if val == "Y" else -1
            if acc not in dic:
                dic[acc] = ind + 1
        return  dic[max(dic.keys())]
       



