class Solution:
    def partitionString(self, s: str) -> int:
        memo = {}
        curr = 0
        for i, x in enumerate(s):
            if memo.get(x, 0) == curr:
                curr += 1
            memo[x] = curr
        return curr
