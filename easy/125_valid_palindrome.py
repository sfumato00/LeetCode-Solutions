class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join([x for x in s.lower() if x.isalnum()])
        return ss == ss[::-1]
