class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        '''
        0. stack emp , len = 1  ans.append( val , flag)
        1. no shit > stack = 0 not,  no comment append(val , flag)
        2.  line comment > append(untilll comet ) ignore  staack = 0 
        3. stack =1  let end one line  
        for i in range(1, lne) #
        '''
        stack = []
        ans = ""
        cur_stack  = -1
        clo_stack = -1
        for i in  source:
            cur_stack  = -1
            clo_stack = -1
            if len(i) == 0:
                continue
            if len(i) == 1 and not stack :
                ans+= i
                ans += "\u00b0"
            elif "/*" not in i and "//" not in i and not stack:
                ans += i
                ans += "\u00b0"
            elif stack and "*/" in i:
                 for ind in range(1, len(i)):
                     if stack and f'{i[ind-1]}{i[ind]}' == "*/" and ind-1 != cur_stack:
                        stack.clear()
                        clo_stack = ind
                        if ind + 1 == len(i):
                            ans += "\u00b0"
                     elif not stack and f'{i[ind-1]}{i[ind]}' == "//" and ind-1 != clo_stack:
                        ans += "\u00b0"
                        break
                     elif f'{i[ind-1]}{i[ind]}' == "/*" and not stack and ind-1 != clo_stack :
                        stack.append(1)
                        cur_stack = ind
                        if "*/" not in i[ind+1:]:
                            break
                        
                     
                     elif not stack :
                        if ind-1 != clo_stack:
                            ans += i[ind-1]
                        if ind +1 == len(i):
                            ans +=  i[ind]
                            ans += "\u00b0"
                     
            elif not stack and "/*" in i or "//" in i:
                for ind in range(1, len(i)):
                    if not stack and f'{i[ind-1]}{i[ind]}' == "//" and ind-1 != clo_stack:
                        ans += "\u00b0"
                        break
                    elif f'{i[ind-1]}{i[ind]}' == "/*" and not stack and ind-1 != clo_stack:
                        stack.append(1)
                        cur_stack = ind
                        if "*/" not in i[ind+1:]:
                            break
                        
                    elif stack and f'{i[ind-1]}{i[ind]}' == "*/" and ind-1 != cur_stack:
                        stack.clear()
                        clo_stack = ind
                        if ind + 1 == len(i):
                            ans += "\u00b0"
                    elif not stack :
                        if ind-1 != clo_stack:
                            ans += i[ind-1]
                        if ind +1 == len(i):
                            ans +=  i[ind]
                            ans += "\u00b0"
        print(ans)
        return [i for i in list(ans.split("\u00b0")) if len(i ) > 0]                        

                    

            

