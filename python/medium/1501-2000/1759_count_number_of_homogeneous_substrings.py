from itertools import groupby


class Solution:
    # def countHomogenous(self, s: str) -> int:
    #     MOD = 1_000_000_007

    #     def cnt(l, r):
    #         n = r - l
    #         return int(n * (n + 1) / 2)

    #     ans, l = 0, 0
    #     for r, ch in enumerate(s):
    #         if ch != s[l]:
    #             ans += cnt(l, r)
    #             l = r
    #     n = len(s)
    #     return (ans + cnt(l, len(s))) % MOD

    def countHomogenous(self, s):
        MOD = 1_000_000_007
        res = 0
        for c, s in groupby(s):
            n = len(list(s))
            res += n * (n + 1) // 2
        return res % MOD
