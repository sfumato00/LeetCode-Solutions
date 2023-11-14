from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        indices = defaultdict(list)

        for i, ch in enumerate(s):
            indices[ch] += [i]

        ans = 0
        for ch, idx in indices.items():
            if len(idx) < 2:
                continue
            start, end = idx[0] + 1, idx[-1]
            unique_letter = set(s[start:end])
            ans += len(unique_letter)        
        return ans