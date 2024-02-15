class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fi = 0
        ten = 0
        tw = 0
    
        for mon in bills:
            if mon == 5:
                fi += 1
            elif mon == 10:
                ten += 1
                if fi:
                    fi -= 1
                else:
                    return False
            else:
                tw += 1
                if fi:
                    if ten:
                        ten -= 1
                        fi -= 1
                    elif fi > 2:
                        fi -= 3
                    else:
                        return False
                else:
                    return False
        return True
                      
                                     
                        

                    
