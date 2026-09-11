from itertools import permutations

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        seen = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            if perm[2] % 2 != 0:
                continue
            num = perm[0]*100 + perm[1]*10 + perm[2]
            seen.add(num)
        return len(seen)