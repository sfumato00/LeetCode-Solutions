from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        cnt1, cnt2 = Counter(s1), Counter(s2[:l1])
        if cnt1 == cnt2:
            return True
        i, j = 0, l1
        while j < l2:
            cnt2[s2[i]] -= 1
            cnt2[s2[j]] += 1
            if cnt1 == cnt2:
                return True
            i += 1
            j += 1
        return False
