class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count = {}
        operations = 0

        for num in nums:
            complement = k - num
            if complement in num_count and num_count[complement] > 0:
                operations += 1
                num_count[complement] -= 1
            else:
                num_count[num] = num_count.get(num, 0) + 1

        return operations

