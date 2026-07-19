class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and ch < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)