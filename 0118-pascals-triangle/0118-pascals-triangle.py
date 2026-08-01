class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]

            ans.append(row)

        return ans