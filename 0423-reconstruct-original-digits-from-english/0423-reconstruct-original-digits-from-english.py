from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        count = [0] * 10
        
        # Unique letters for these digits:
        count[0] = c['z']                          # zero
        count[2] = c['w']                          # two
        count[4] = c['u']                          # four
        count[6] = c['x']                          # six
        count[8] = c['g']                          # eight
        
        count[3] = c['h'] - count[8]                # three (h also in eight)
        count[5] = c['f'] - count[4]                # five (f also in four)
        count[7] = c['s'] - count[6]                # seven (s also in six)
        
        count[1] = c['o'] - count[0] - count[2] - count[4]   # one (o also in zero, two, four)
        count[9] = c['i'] - count[5] - count[6] - count[8]   # nine (i also in five, six, eight)
        
        result = []
        for digit in range(10):
            result.append(str(digit) * count[digit])
        
        return ''.join(result)