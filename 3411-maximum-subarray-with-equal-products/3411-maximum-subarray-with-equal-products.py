class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd, lcm

        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans