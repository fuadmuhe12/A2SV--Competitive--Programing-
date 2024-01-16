class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        '''
        1. have a dictionary that store the last index of eaach ans
        2. have two pointer and count the number of true and flase andas long as one of them id less than or equal to k keep moving 
        3. if it is greater then cur size was end -start  then the start will be at the mininmum index +1 in the dictionary of values 

        '''
        start  = 0
        end = 0
        T = 0
        F = 0
        mx = 0
        while end  < len(answerKey):
            if answerKey[end] == 'T':
                T += 1
            else:
                F += 1
            while not  (F <= k or T <= k ):
                if answerKey[start] == 'T':
                    T -= 1
                else:
                    F -= 1
                start += 1
            mx = max(mx, end -start + 1)
            end += 1
            
        return mx
            

            
                


