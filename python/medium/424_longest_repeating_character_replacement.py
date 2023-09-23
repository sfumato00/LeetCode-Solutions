from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        lo, max_freq = 0, 0
        for hi, ch in enumerate(s):
            cnt[ch] += 1
            max_freq = max(max_freq, cnt[ch])
            if max_freq + k < hi - lo + 1:
                cnt[s[lo]] -= 1
                lo += 1
        return len(s) - lo
