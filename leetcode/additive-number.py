class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        def backtrack(ind, lval, lsum, coun):
            
            if ind is None:
                for fir in range(0, len(num)):
                    if  not (num[0] != '0' or num[fir] == '0'):
                        continue
                    for sec in range(fir +1, len(num)):
                        if (num[fir+1] == '0' and num[sec] != '0')  :
                            continue
                        a = int(num[fir+1:sec+1])
                        b = int(num[:fir+1])
                        coun += 1
                        if backtrack(sec + 1, a , a + b, coun):
                            return True
                        coun -= 1
            if ind  and ind >= len(num) and coun > 1:
                return True
            if ind and  ind >= len(num) :
                return 
            if ind:
                for i in range(ind, len(num)):
                    if int (num[ind: i +1]) == lsum and (num[ind] != '0' or num[i] == '0'):

                        curval = int (num[ind: i +1])
                        cursum = lval + curval
                        coun += 1
                        return backtrack(i +1,curval,cursum, coun)
                        coun -= 1
                return False
        return backtrack(None,None,None, 0)

            


        

                    

        
        
        