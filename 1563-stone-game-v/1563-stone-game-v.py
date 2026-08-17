from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:

        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(l, r):
            if l >= r:
                return 0

            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]
            best = 0

            for k in range(l, r):

                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:

                    # If even 2 * left_sum can't improve best,
                    # this split isn't useful.
                    if best >= 2 * left_sum:
                        continue

                    best = max(
                        best,
                        left_sum + dp(l, k)
                    )

                elif left_sum > right_sum:

                    # Future right_sum will only become smaller.
                    # So if current best is already >= 2 * right_sum,
                    # no future split can improve it.
                    if best >= 2 * right_sum:
                        break

                    best = max(
                        best,
                        right_sum + dp(k + 1, r)
                    )

                else:
                    best = max(
                        best,
                        left_sum + dp(l, k),
                        right_sum + dp(k + 1, r)
                    )

            return best

        return dp(0, len(stoneValue) - 1)