# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        subseq_lengths = defaultdict(int)
        max_length = 1

        for num in arr:
            prev_num = num - difference
            subseq_lengths[num] = subseq_lengths[prev_num] + 1
            max_length = max(max_length, subseq_lengths[num])

        return max_length