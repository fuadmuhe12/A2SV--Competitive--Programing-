class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_prex  = [0]*len(s)
        for start, end , val in shifts :
            if val:
                shift_prex[start] += 1
                if end != len(s)-1:
                    shift_prex[end+1] -= 1
            else:
                shift_prex[start] -= 1
                if end != len(s)-1:
                    shift_prex[end+1] += 1
        accu = 0
        prefix = [0]* len(s)
        
        for  ind ,val in enumerate(shift_prex):
            accu += val
            prefix[ind] = accu

        


        alphabet_to_number = {
            0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
            10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
            20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'
        }
        number_to_alphabet = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
        }
        res = []
        for ind, val  in enumerate(s):
            num =  number_to_alphabet[val]
            num += prefix[ind]
            ans = alphabet_to_number[num%26]
            res.append(ans)
        return "".join(res)






