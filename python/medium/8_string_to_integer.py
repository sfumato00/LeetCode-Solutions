class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        sign = 1
        num = 0
        i = 0
        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return num

        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        thresh = 2**31 - 1
        while i < n and s[i].isdigit():
            x = int(s[i])

            # python doesn't need it but we should show that we are mindful of the overflow problem some language might have
            if sign > 0 and num >= (thresh - x) / 10:
                return thresh

            if sign < 0 and num >= (thresh - x + 1) / 10:
                return -thresh - 1

            num = num * 10 + int(s[i])
            i += 1

        return sign * num
