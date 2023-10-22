class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        inc_dp = [1] * n  # inc_dp[i] represents the length of the turbulent subarray ending at index i with an increasing sequence
        dec_dp = [1] * n  # dec_dp[i] represents the length of the turbulent subarray ending at index i with a decreasing sequence

        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                inc_dp[i] = dec_dp[i - 1] + 1
            elif arr[i - 1] > arr[i]:
                dec_dp[i] = inc_dp[i - 1] + 1

        return max(max(inc_dp), max(dec_dp))
