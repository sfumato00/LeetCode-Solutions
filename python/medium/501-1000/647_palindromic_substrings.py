class Solution:
    def countSubstrings(self, s: str) -> int:
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # out = 0
        # for l in range(n):
        #     for i in range(n - l):
        #         j = i + l
        #         if s[i] == s[j]:
        #             dp[i][j] = j - i <= 2 or dp[i + 1][j - 1]
        #             out += 1 if dp[i][j] else 0
        # return out

        n = len(s)
        count = 0

        def search(lo, hi):
            nonlocal count
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1

        for i in range(n):
            search(i, i)
            search(i, i + 1)
        return count
