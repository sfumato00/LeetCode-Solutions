class Solution:
    def calculate(self, s: str) -> int:
        s += "#"
        z = ord("0")
        total, num = 0, 0
        stk = []
        op = "+"
        for x in s:
            if x == " ":
                continue

            if x.isdigit():
                num = num * 10 + ord(x) - z
                continue

            if op == "+":
                total += num
            elif op == "-":
                total -= num

            if x == "+" or x == "-":
                op = x
            elif x == "(":
                stk += [total]
                total = 0
                stk += [op]
                op = "+"
            elif x == ")":
                _op = stk.pop()
                if _op == "+":
                    total += stk.pop()
                else:
                    total = stk.pop() - total
            num = 0
        return total
