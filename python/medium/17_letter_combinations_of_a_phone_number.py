from collections import defaultdict
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return None

        mapping = defaultdict(
            str,
            {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
            },
        )

        ans, curr = [], []
        n = len(digits)

        def dfs(pos):
            if pos == n:
                ans.append("".join(curr))
                return

            d = digits[pos]
            for ch in mapping[d]:
                curr.append(ch)
                dfs(pos + 1)
                curr.pop()

        dfs(0)
        return ans
