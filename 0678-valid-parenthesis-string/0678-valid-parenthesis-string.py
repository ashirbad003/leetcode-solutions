class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0  # open brackets ki minimum / maximum possible count
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*' ya to ')' ya '(' ya khaali
                lo -= 1
                hi += 1
            if hi < 0:      # ')' zyada ho gaye, koi '*' bhi bacha nahi sakta
                return False
            if lo < 0:      # negative open count possible nahi
                lo = 0
        return lo == 0