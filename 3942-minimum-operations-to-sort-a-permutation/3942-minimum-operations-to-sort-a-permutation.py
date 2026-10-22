from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        rev = nums[::-1]

        # Find which (f, j) states, if any, give the sorted array
        targets = []
        j0 = (-nums[0]) % n
        if all(nums[m] == (m - j0) % n for m in range(n)):
            targets.append((0, j0))

        j1 = (-rev[0]) % n
        if all(rev[m] == (m - j1) % n for m in range(n)):
            targets.append((1, j1))

        if not targets:
            return -1

        # BFS over 2n abstract states
        dist = [[-1] * n for _ in range(2)]
        dist[0][0] = 0
        q = deque([(0, 0)])

        while q:
            f, j = q.popleft()
            d = dist[f][j]

            # Operation: rotate left by one
            nj = (j + 1) % n
            if dist[f][nj] == -1:
                dist[f][nj] = d + 1
                q.append((f, nj))

            # Operation: reverse
            nf, rj = 1 - f, (-j) % n
            if dist[nf][rj] == -1:
                dist[nf][rj] = d + 1
                q.append((nf, rj))

        answers = [dist[f][j] for f, j in targets if dist[f][j] != -1]
        return min(answers) if answers else -1