from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) < len(t):
            s, t = t, s
        return next(iter(Counter(s) - Counter(t)))
