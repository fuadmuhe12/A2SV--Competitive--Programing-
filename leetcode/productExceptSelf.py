class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n

        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            left_products[i] = left_product

        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product

        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer
