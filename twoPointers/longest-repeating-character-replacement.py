from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        max_len = 0
        max_freq = 0
        start = 0

        for end in range(len(s)):
            char_count[s[end]] += 1
            max_freq = max(max_freq, char_count[s[end]])

            if end - start + 1 - max_freq > k:
                char_count[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
