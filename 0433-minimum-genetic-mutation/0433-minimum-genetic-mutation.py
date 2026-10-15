from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for c in "ACGT":
                    if c == gene[i]:
                        continue
                    mutated = gene[:i] + c + gene[i+1:]
                    if mutated in bank_set and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, steps + 1))

        return -1