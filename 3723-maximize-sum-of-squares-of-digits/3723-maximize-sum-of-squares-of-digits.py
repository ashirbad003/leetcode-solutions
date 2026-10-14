class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Each digit is at most 9, so the total must fit
        if sum > 9 * num:
            return ""

        digits = []
        remaining = sum
        for i in range(num):
            # Digits left after this position (each can hold up to 9)
            left = num - i - 1
            # Place the largest digit possible, but keep the rest feasible
            d = min(9, remaining)
            digits.append(str(d))
            remaining -= d

        return "".join(digits)