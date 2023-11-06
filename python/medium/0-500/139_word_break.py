from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {k: True for k in wordDict}

        def dfs(s):
            if s in memo:
                return memo[s]

            for i in range(len(s)):
                if memo.get(s[i:], False) and dfs(s[:i]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False

        return dfs(s)


class SolutionBad:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)

        @lru_cache
        def dfs(s):
            return not s or any([s[i:] in dic and dfs(s[:i]) for i in range(len(s))])

        return dfs(s)
