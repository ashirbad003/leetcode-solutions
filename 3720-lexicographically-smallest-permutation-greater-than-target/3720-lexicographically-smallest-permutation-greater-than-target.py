class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        
        orig = [0] * 26
        for ch in s:
            orig[ord(ch) - 97] += 1
        
        # Find max feasible prefix length L: how far target can be matched using s's letters
        work = orig[:]
        L = 0
        for j in range(n):
            idx = ord(target[j]) - 97
            if work[idx] > 0:
                work[idx] -= 1
                L += 1
            else:
                break
        
        # prefix_count[i] = counts of characters in target[0:i]
        prefix_count = [[0] * 26]
        counts = [0] * 26
        for j in range(n):
            counts = counts[:]
            counts[ord(target[j]) - 97] += 1
            prefix_count.append(counts)
        
        max_i = min(L, n - 1)
        
        for i in range(max_i, -1, -1):
            freq = orig[:]
            pc = prefix_count[i]
            for c in range(26):
                freq[c] -= pc[c]
            
            t_idx = ord(target[i]) - 97
            chosen = -1
            for c in range(t_idx + 1, 26):
                if freq[c] > 0:
                    chosen = c
                    break
            
            if chosen != -1:
                freq[chosen] -= 1
                result = list(target[:i])
                result.append(chr(chosen + 97))
                for c in range(26):
                    result.extend([chr(c + 97)] * freq[c])
                return ''.join(result)
        
        return ""