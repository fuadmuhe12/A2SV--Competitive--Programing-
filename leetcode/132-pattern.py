class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        max_val = float('-inf')

        for i in range(n - 1, -1, -1):
            if nums[i] < max_val:
                return True  # Found a 132 pattern

            while stack and nums[i] > stack[-1]:
                max_val = stack.pop()

            stack.append(nums[i])

        return False


