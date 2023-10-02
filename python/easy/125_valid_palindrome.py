class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join([x for x in s.lower() if x.isalnum()])
        return ss == ss[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1

            if lo < hi and s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
