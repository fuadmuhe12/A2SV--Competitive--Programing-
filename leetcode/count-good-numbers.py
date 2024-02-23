class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ' _1__ ___'
        eve = n//2 if n%2 == 0 else n//2 + 1
        odd = n // 2
        bi = bin(eve)[2:]
        ans = 1
        MOD = 10**9 + 7
        ##########
        def mod_pow(base, exponent, modulo):
            result = 1

            # Ensure exponent is non-negative
            exponent = max(0, exponent)

            while exponent > 0:
                # If the least significant bit is 1, multiply by base
                if exponent % 2 == 1:
                    result = (result * base) % modulo

                # Square the base and reduce the exponent by half
                base = (base * base) % modulo
                exponent //= 2

            return result
        ##########
        return (mod_pow(4, odd, MOD) * mod_pow(5, eve, MOD)) %MOD
