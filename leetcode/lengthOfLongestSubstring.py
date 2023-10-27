class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        a = 0
        b = 0
        max_length = 0

        while b < len(s):
            if s[b] not in char_index or char_index[s[b]] < a:
                char_index[s[b]] = b
                b += 1
                max_length = max(max_length, b - a)
            else:
                a = char_index[s[b]] + 1

        return max_length




        

        
