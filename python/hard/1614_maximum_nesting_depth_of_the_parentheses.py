class Solution:
    def maxDepth(self, s: str) -> int:
        ans, bal = 0, 0
        for x in s:
            if x == "(":
                bal += 1
                ans = max(ans, bal)
            elif x == ")":
                bal -= 1
        return ans
