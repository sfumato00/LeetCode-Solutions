from functools import cache


class Memorization:
    @cache
    def integerBreak(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 1

        ret = n - 1
        # r = n // 2 + 1
        for i in range(2, n):
            ret = max(ret, i * (n - i), i * self.integerBreak(n - i))
        return ret


class DP:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        dp[0:4] = [0, 1, 2, 3]

        for i in range(4, n + 1):
            for j in range(2, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[n]
