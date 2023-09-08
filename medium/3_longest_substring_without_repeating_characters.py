from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(lambda: -1)
        ans, lo = 0, 0
        for hi, ch in enumerate(s):
            if seen[ch] < lo:
                ans = max(ans, hi - lo + 1)
            else:
                lo = seen[ch] + 1
            seen[ch] = hi
        return ans
