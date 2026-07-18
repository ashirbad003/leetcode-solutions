class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        goingDown = False

        for ch in s:
            rows[currRow] += ch

            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currRow += 1
            else:
                currRow -= 1

        return "".join(rows)