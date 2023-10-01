class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False

        def is_integer(s):
            if not s:
                return False

            if s[0] == "-" or s[0] == "+":
                return is_unsigned_integer(s[1:])
            return is_unsigned_integer(s)

        def is_unsigned_integer(s):
            if not s:
                return False
            for i, x in enumerate(s):
                if not x.isdigit():
                    return False
            return True

        terms = s.lower().split("e")
        m = len(terms)
        if m > 2:
            return False
        if m > 1 and not is_integer(terms[1]):
            return False

        s = terms[0]

        coms = s.split(".")
        n = len(coms)

        if n == 1:
            return is_integer(coms[0])

        if n == 2:
            if not coms[0] and not coms[1]:
                return False
            elif not coms[1]:
                return is_integer(coms[0])
            elif not coms[0]:
                return is_unsigned_integer(coms[1])
            return is_unsigned_integer(coms[1]) and (
                coms[0] in ["+", "-"] or is_integer(coms[0])
            )

        return False
