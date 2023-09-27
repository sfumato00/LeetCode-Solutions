class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        i, n = 0, len(s)
        while i < n:
            _max = i
            for j in range(n - 1, i, -1):
                if s[j] > s[_max]:
                    _max = j

            if _max != i:
                s[i], s[_max] = s[_max], s[i]
                return int("".join(s))
            i += 1
        return num
