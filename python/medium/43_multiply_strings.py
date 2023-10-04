class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        out = 0
        base1 = 1
        for x in reversed(num1):
            base2 = base1
            for y in reversed(num2):
                out += int(x) * int(y) * base2
                base2 *= 10
            base1 *= 10
        return str(out)
