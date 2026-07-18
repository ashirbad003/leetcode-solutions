class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        b = (r // 3) * 3 + c // 3
                        for ch in "123456789":
                            if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                                board[r][c] = ch
                                rows[r].add(ch)
                                cols[c].add(ch)
                                boxes[b].add(ch)

                                if backtrack():
                                    return True

                                board[r][c] = "."
                                rows[r].remove(ch)
                                cols[c].remove(ch)
                                boxes[b].remove(ch)
                        return False
            return True

        backtrack()