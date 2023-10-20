class Solution:
    def minInsertions(self, s: str) -> int:
        bal, ans = 0, 0
        s = s.replace("))", "}")

        for x in s:
            if x == "(":
                bal += 1

            else:
                if x == ")":
                    ans += 1

                bal -= 1

                if bal < 0:
                    ans += 1
                    bal = 0

        return bal * 2 + ans
