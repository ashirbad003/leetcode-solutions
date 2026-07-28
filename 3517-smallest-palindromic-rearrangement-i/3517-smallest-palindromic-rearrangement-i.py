from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        left = []
        middle = ""

        for ch in sorted(count):
            left.append(ch * (count[ch] // 2))
            if count[ch] % 2 == 1:
                middle = ch

        left = "".join(left)
        return left + middle + left[::-1]