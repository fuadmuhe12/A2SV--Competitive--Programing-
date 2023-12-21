class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        '''
        1. for each of the len(s[0]) prepare place [[] for i i]

        '''
        delet =set()
        stack = [[] for i in range(len(strs[0]))] 
        for i in range(len(strs[0])):
            stack[i].append(strs[0][i])
        cols = len(strs[0])
        for row in range(1, len(strs)):
            for col in range(cols):
                if col in delet:
                    continue
                else:
                    if stack[col][-1] > strs[row][col]:
                       delet.add(col)
                    else:
                        stack[col].append(strs[row][col])

        return len(delet)

