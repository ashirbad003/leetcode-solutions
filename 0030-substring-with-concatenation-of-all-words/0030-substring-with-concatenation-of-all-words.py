from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        target = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            curr = Counter()
            count = 0

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    curr[word] += 1
                    count += 1

                    while curr[word] > target[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        res.append(left)
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    curr.clear()
                    count = 0
                    left = right + word_len

        return res