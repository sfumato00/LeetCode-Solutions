class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        for i, x in enumerate(s):
            if x == "(":
                stk += [i]
            else:
                if stk and s[stk[-1]] == "(":
                    stk.pop()  # pop valid parenthesis pairs
                else:
                    stk += [i]

        stk += [len(s)]  # padding for edge conditions
        last = -1  # for edge condition

        ans = 0
        for i in stk:
            ans = max(ans, i - last - 1)
            last = i

        return ans
