class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        m = len(s)
        i = m - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1

        if i == -1:
            return -1

        j = m - 1
        while j > i and s[j] <= s[i]:
            j -= 1

        s[i], s[j] = s[j], s[i]
        lo, hi = i + 1, m - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        x = int("".join(s))
        return x if x < 2**31 else -1
