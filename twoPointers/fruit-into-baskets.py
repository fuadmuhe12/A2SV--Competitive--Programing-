class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        ind_dic =  {}
        mx = 0
        to_del = 0
        while end < len(fruits):
            while end < len(fruits) and len(ind_dic) < 3:
                if len(ind_dic) == 2 and fruits[end] not in ind_dic:
                    mx = max(mx, end-start)
                    start = ind_dic[fruits[min(ind_dic.values())]]+1
                    del ind_dic[fruits[min(ind_dic.values())]]
                    ind_dic[fruits[end]] = end
                    end+=1

                   
                else:
                    ind_dic[fruits[end]] = end
                    end += 1
                    
                
            mx = max(mx, end-start)
            start = ind_dic[fruits[min(ind_dic.values())]]+1
            del ind_dic[fruits[min(ind_dic.values())]]
            
        return mx


                
           
            
            



