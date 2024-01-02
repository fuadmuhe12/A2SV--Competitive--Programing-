from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            current_sum = numbers[start] + numbers[end]

            if current_sum == target:
                return [start + 1, end + 1]
            elif current_sum < target:
                start += 1
            else:
                end -= 1

        # If no solution is found
        return [-1, -1]
