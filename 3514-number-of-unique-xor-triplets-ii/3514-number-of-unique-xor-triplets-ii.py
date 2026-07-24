from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))
        MAXX = 2048

        pair = [False] * MAXX

        # All possible XORs of two values
        for a in vals:
            for b in vals:
                pair[a ^ b] = True

        ans = [False] * MAXX

        # XOR with the third value
        for x in range(MAXX):
            if pair[x]:
                for v in vals:
                    ans[x ^ v] = True

        return sum(ans)