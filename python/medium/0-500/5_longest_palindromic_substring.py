class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [0, 0]

        def check(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > ans[1] - ans[0]:
                    ans[:] = [l, r + 1]
                l, r = l - 1, r + 1

        for i in range(n):
            check(i, i)
            check(i, i + 1)

        return s[ans[0] : ans[1]]
