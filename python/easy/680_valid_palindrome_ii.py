class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1

        while lo < hi and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        s1 = s[:lo] + s[lo + 1 :]
        s2 = s[:hi] + s[hi + 1 :]
        return lo == hi or s1 == s1[::-1] or s2 == s2[::-1]
