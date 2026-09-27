class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        x, y = nums[:n], nums[n:]
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        return result