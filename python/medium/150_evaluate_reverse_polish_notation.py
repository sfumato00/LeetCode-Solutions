from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = ["+", "-", "*", "/"]
        for x in tokens:
            if x not in ops:
                stk += [int(x)]
            else:
                b = stk.pop()
                a = stk.pop()
                if x == "+":
                    stk += [a + b]
                elif x == "-":
                    stk += [a - b]
                elif x == "*":
                    stk += [a * b]
                elif x == "/":
                    stk += [int(a / b)]
        return stk[-1]
