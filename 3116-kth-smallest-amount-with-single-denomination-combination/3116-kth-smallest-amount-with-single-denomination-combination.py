from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def count_le(x):
            # Count how many numbers <= x are achievable using at least one coin
            # via inclusion-exclusion over all non-empty subsets of coins
            total = 0
            for mask in range(1, 1 << n):
                lcm_val = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm_val = lcm_val * coins[i] // gcd(lcm_val, coins[i])
                        if lcm_val > x:
                            break
                if lcm_val > x:
                    continue
                if bits % 2 == 1:
                    total += x // lcm_val
                else:
                    total -= x // lcm_val
            return total
        
        low, high = 1, min(coins) * k
        
        while low < high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low