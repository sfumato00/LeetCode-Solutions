class Solution:
    zero = ord("0")

    def calculate(self, s: str) -> int:
        s += "#"
        op = "+"
        res, temp, number = 0, 0, 0
        for x in s:
            if x == " ":
                continue

            if x.isdigit():
                number = number * 10 + (ord(x) - Solution.zero)
                continue

            if op == "+":
                res += temp
                temp = number
            elif op == "-":
                res += temp
                temp = -number
            elif op == "*":
                temp *= number
            elif op == "/":
                temp = int(temp / number)

            number = 0
            op = x

        return res + temp
