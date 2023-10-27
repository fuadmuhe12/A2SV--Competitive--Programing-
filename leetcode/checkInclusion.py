class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        def is_permutation(window, s1_count):
            return window == s1_count

        # Initialize character count for s1 and the sliding window
        s1_count = [0] * 26
        window_count = [0] * 26

        # Count characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        # Initialize the sliding window
        for i in range(len_s1):
            window_count[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if is_permutation(window_count, s1_count):
            return True

        # Slide the window through the rest of s2
        for i in range(len_s1, len_s2):
            window_count[ord(s2[i - len_s1]) - ord('a')] -= 1
            window_count[ord(s2[i]) - ord('a')] += 1
            if is_permutation(window_count, s1_count):
                return True

        return False

