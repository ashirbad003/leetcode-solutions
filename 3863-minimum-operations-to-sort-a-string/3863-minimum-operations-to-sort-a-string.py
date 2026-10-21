class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = ''.join(sorted(s))
        if s == t:
            return 0
        L = next(i for i in range(n) if s[i] != t[i])
        R = max(i for i in range(n) if s[i] != t[i])
        if (L, R) != (0, n - 1):
            return 1
        if n == 2:
            return -1
        if t[0] in s[:-1] or t[-1] in s[1:]:
            return 2
        return 3