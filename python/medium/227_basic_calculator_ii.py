class Solution:
    def calculate(self, s: str) -> int:
        s = s + "+"
        output, term, num = 0, 0, 0
        op = "+"
        for i, x in enumerate(s):
            if x == " ":
                continue

            if x.isdigit():
                num = num * 10 + int(x)
                continue

            if op == "+":
                output, term = output + term, num
            elif op == "-":
                output, term = output + term, -num
            elif op == "*":
                term *= num
            elif op == "/":
                term = int(term / num)
            num = 0
            op = x
        return output + term
