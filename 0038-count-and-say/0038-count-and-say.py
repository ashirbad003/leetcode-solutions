class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            res = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(s[i - 1])
                    count = 1

            res.append(str(count))
            res.append(s[-1])
            s = "".join(res)

        return s