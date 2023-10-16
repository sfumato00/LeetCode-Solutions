class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        return BottomUpSolution().numWays(steps, arrLen)


class TopDownSolution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def nums_ways(steps, pos):
            if steps == 0 and pos == 0:
                return 1

            if steps < 0 or pos == arrLen or pos < 0:
                return 0

            return (
                nums_ways(steps - 1, pos + 1)
                + nums_ways(steps - 1, pos - 1)
                + nums_ways(steps - 1, pos)
            ) % 1_000_000_007

        return nums_ways(steps, 0)


class BottomUpSolution:
    def numWays(self, steps: int, arrLen: int) -> int:
        l = min(steps, arrLen)
        prev, curr = [0] * l, [0] * l
        prev[0] = 1

        for i in range(steps):
            for j in range(l):
                curr[j] = prev[j]
                if j > 0:
                    curr[j] += prev[j - 1]
                if j < l - 1:
                    curr[j] += prev[j + 1]
            curr, prev = prev, curr
        return prev[0] % 1_000_000_007
