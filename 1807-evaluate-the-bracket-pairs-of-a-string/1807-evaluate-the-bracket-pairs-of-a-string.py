class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv = {k: v for k, v in knowledge}
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i+1:j]
                result.append(kv.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        
        return ''.join(result)