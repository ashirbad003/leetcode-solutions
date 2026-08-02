from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        @lru_cache(None)
        def dfs(start):
            if start == len(s):
                return [""]

            res = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for suffix in dfs(end):
                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)

            return res

        return dfs(0)