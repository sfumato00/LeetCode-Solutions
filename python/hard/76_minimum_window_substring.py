from math import inf
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if m > n:
            return ""
        cnt = Counter(t)
        l = 0
        ans = [-1, inf]
        for r, ch in enumerate(s):
            if ch not in cnt:
                continue

            if cnt[ch] > 0:
                m -= 1
            cnt[ch] -= 1

            while m == 0:
                if s[l] in cnt:
                    ln = r - l + 1
                    if ln < ans[1] - ans[0] + 1:
                        ans[:] = [l, r]
                    cnt[s[l]] += 1
                    if cnt[s[l]] > 0:
                        m += 1
                l += 1
        l, r = ans
        return s[l : r + 1] if r != inf else ""
