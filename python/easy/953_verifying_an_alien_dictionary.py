class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {x: i for i, x in enumerate(order)}

        def le(w1, w2):
            m, n = len(w1), len(w2)
            i, l = 0, min(m, n)
            while i < l:
                if d[w1[i]] < d[w2[i]]:
                    return True
                if d[w1[i]] > d[w2[i]]:
                    return False
                i += 1
            return m <= n

        for w1, w2 in zip(words, words[1:]):
            if not le(w1, w2):
                return False
        return True
