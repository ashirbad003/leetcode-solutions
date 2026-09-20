class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, 1):
            total += (26 - (ord(ch) - ord('a'))) * i
        return total