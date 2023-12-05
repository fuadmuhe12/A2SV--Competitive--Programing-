class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        one = set("qwertyuiop")
        two =  set("asdfghjkl")
        three = set("zxcvbnm")
        return  [i for i in words if set(i.lower()).issubset(one) or set(i.lower()).issubset(two) or set(i.lower()).issubset(three)]
       