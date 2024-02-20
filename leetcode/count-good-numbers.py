class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, y, mod):
            result = 1
            x = x % mod
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % mod
                y = y // 2
                x = (x * x) % mod
            return result

        even_count = power(5, (n + 1) // 2, 10**9 + 7)
        odd_count = power(4, n // 2, 10**9 + 7)

        total_good_numbers = (even_count * odd_count) % (10**9 + 7)
        return total_good_numbers
    
        countGoodNumbers(n)

