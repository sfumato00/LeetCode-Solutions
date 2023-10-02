from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict = set(wordDict)

        @lru_cache()
        def _break(s: str) -> List[List[str]]:
            if not s:
                return []

            out = []
            for i in range(len(s)):
                prefix, suffix = s[:i], s[i:]
                if suffix not in word_dict:
                    continue

                if i == 0:
                    out += [[suffix]]
                    continue

                for pre in _break(prefix):
                    out += [pre + [suffix]]
            return out

        return [" ".join(p) for p in _break(s)]
