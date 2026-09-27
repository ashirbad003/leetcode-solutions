class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                inner = stack.pop()
                inner.reverse()
                stack[-1].extend(inner)
            else:
                stack[-1].append(ch)
        return ''.join(stack[-1])