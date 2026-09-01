from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = (i, j)

                elif classroom[i][j] == "L":
                    litter[(i, j)] = count
                    count += 1

        target = (1 << count) - 1

        # (row, column, remaining_energy, collected_mask)
        queue = deque([
            (start[0], start[1], energy, 0)
        ])

        # Stores the maximum energy seen for (row, column, mask)
        best_energy = {
            (start[0], start[1], 0): energy
        }

        moves = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            for _ in range(len(queue)):
                x, y, remaining, mask = queue.popleft()

                if mask == target:
                    return moves

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if classroom[nx][ny] == "X":
                        continue

                    if remaining == 0:
                        continue

                    new_energy = remaining - 1
                    new_mask = mask

                    # Collect litter
                    if (nx, ny) in litter:
                        new_mask |= (1 << litter[(nx, ny)])

                    # Recharge
                    if classroom[nx][ny] == "R":
                        new_energy = energy

                    state = (nx, ny, new_mask)

                    # Skip if we already reached this state
                    # with equal or more energy
                    if (
                        state in best_energy
                        and best_energy[state] >= new_energy
                    ):
                        continue

                    best_energy[state] = new_energy
                    queue.append(
                        (nx, ny, new_energy, new_mask)
                    )

            moves += 1

        return -1