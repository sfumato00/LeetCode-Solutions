class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)

        i, j = m - 1, n - 1
        carry = 0
        output = []
        while i >= 0 and j >= 0:
            carry, x = divmod(int(num1[i]) + int(num2[j]) + carry, 10)
            output += [str(x)]
            i -= 1
            j -= 1

        while i >= 0:
            carry, x = divmod(int(num1[i]) + carry, 10)
            output += [str(x)]
            i -= 1

        while j >= 0:
            carry, x = divmod(int(num2[j]) + carry, 10)
            output += [str(x)]
            j -= 1
        if carry > 0:
            output += [str(carry)]
        return "".join(output[::-1])
