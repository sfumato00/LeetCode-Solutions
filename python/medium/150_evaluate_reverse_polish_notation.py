from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def op(ch: str, val1: int, val2: int):
            if ch == "+":
                return val1 + val2
            if ch == "-":
                return val1 - val2
            if ch == "*":
                return val1 * val2
            if ch == "/":
                return int(val1 / val2)

        stk = []
        signs = ["+", "-", "*", "/"]
        for x in tokens:
            if x in signs:
                val2, val1 = stk.pop(), stk.pop()
                stk.append(op(x, val1, val2))
            else:
                stk.append(int(x))
        return stk.pop()
