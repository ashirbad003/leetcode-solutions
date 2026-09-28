class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        return max_depth