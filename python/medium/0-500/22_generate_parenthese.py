from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r):
            if l == r == n:
                ans.append("".join(curr))
                return

            if l < n:
                curr.append("(")
                dfs(l + 1, r)
                curr.pop()

            if r < l:
                curr.append(")")
                dfs(l, r + 1)
                curr.pop()

        ans, curr = [], []
        dfs(0, 0)
        return ans
