class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for l in range(1, 4):
                if start + l > len(s):
                    break
                part = s[start:start + l]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(start + l, path + [part])

        backtrack(0, [])
        return res