class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        d = 1
        while 10 ** (d - 1) <= n:
            lo = 10 ** (d - 1)
            hi = min(10 ** d - 1, n)
            count_numbers = hi - lo + 1
            commas_per_number = (d - 1) // 3
            total += count_numbers * commas_per_number
            d += 1
        return total