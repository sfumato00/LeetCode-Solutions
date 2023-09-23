from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)
        ans, curr = [], []

        def generate_solution():
            return ["".join(["Q" if i == x else "." for i in range(n)]) for x in curr]

        def dfs(r):
            if r == n:
                ans.append(generate_solution())
                return

            for c in range(n):
                if cols[c] or diag1[r + n - c - 1] or diag2[r + c]:
                    continue

                cols[c] = True
                diag1[r + n - c - 1] = True
                diag2[r + c] = True
                curr.append(c)
                dfs(r + 1)
                curr.pop()
                cols[c] = False
                diag1[r + n - c - 1] = False
                diag2[r + c] = False

        dfs(0)
        return ans
