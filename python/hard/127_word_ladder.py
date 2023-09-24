from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        char_a = ord("a")
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        if beginWord == endWord:
            return 1

        dq1, dq2 = deque([beginWord]), deque([endWord])
        visited1, visited2 = set([beginWord]), set([endWord])
        steps1, steps2, k = 0, 0, len(beginWord)

        while dq1:
            n = len(dq1)
            steps1 += 1
            for _ in range(n):
                w = dq1.popleft()
                for i in range(k):
                    for j in range(26):
                        ch = chr(char_a + j)
                        if ch == w[i]:
                            continue
                        ww = w[:i] + ch + w[i + 1 :]

                        if ww in visited2:
                            return steps1 + steps2 + 1

                        if ww in word_set:
                            dq1.append(ww)
                            word_set.remove(ww)
                            visited1.add(ww)

            if len(dq1) > len(dq2):
                dq1, dq2 = dq2, dq1
                steps1, steps2 = steps2, steps1
                visited1, visited2 = visited2, visited1
        return 0
