class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans, bal = 0, 0
        for x in s:
            if x == "(":
                bal += 1
            elif x == ")":
                if bal <= 0:
                    ans += 1
                else:
                    bal -= 1
        return ans + bal
