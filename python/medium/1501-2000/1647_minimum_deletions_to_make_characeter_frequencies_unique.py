from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        freq = set()
        ans = 0
        for v in cnt.values():
            f = v
            while f in freq:
                f -= 1
            if f > 0:
                freq.add(f)
            ans += v - f
        return ans
