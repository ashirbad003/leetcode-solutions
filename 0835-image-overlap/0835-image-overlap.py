from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        count = defaultdict(int)
        best = 0
        for x1, y1 in ones1:
            for x2, y2 in ones2:
                dx, dy = x1 - x2, y1 - y2
                count[(dx, dy)] += 1
                best = max(best, count[(dx, dy)])
        return best