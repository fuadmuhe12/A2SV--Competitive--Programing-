class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return  []
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
        
        ans  =  []
        def backtrack(ind, temp):
            if ind >= len(digits):
                ans.append(temp[:])
                return 
            
            for val  in dic[digits[ind]]:
                temp.append(val)
                backtrack(ind + 1, temp)
                temp.pop()
        backtrack(0, [])
        return  [''.join(i) for i in ans] if ans  else []

            


            
                