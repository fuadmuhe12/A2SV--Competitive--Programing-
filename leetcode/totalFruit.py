from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        basket_types = {}

        max_fruits = 0

        while end < len(fruits):
            current_fruit = fruits[end]

            # Update the basket types
            basket_types[current_fruit] = end

            # If there are more than 2 types of fruits, adjust the start pointer
            if len(basket_types) > 2:
                start = min(basket_types.values()) + 1
                del basket_types[fruits[start - 1]]

            # Update the maximum number of fruits
            max_fruits = max(max_fruits, end - start + 1)

            end += 1

        return max_fruits

# Test cases
solution = Solution()
print(solution.totalFruit([1,2,1]))  # Output: 3
print(solution.totalFruit([0,1,2,2]))  # Output: 3
print(solution.totalFruit([1,2,3,2,2]))  # Output: 4
