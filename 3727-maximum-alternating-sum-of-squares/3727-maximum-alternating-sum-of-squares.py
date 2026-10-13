class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        n = len(squares)
        plus_count = (n + 1) // 2  # number of even indices

        positive = sum(squares[n - plus_count:])
        negative = sum(squares[:n - plus_count])
        return positive - negative