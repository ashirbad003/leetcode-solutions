class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        need = 0  # kitne ')' chahiye abhi tak ke '(' ko close karne ke liye
        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    # pichla '(' ko sirf ek ')' mila, ek aur insert karo
                    res += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    # koi '(' nahi mila, insert karo
                    res += 1
                    need += 2
        return res + need