from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        start = 0
        end = 1
        n = len(chars)
        
        while end < n:
            if chars[start] == chars[end]:
                end += 1
            else:
                s += chars[start]
                if end - start > 1:
                    s += str(end - start)
                start = end
                end += 1

        # Handle the last group of characters
        s += chars[start]
        if end - start > 1:
            s += str(end - start)

        # Update the input array with the compressed string
        chars[:len(s)] = list(s)

        return len(s)
