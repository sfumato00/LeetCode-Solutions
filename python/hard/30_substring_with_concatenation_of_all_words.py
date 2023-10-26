# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not s or not words:
#             return []

#         n, k, word_len = len(s), len(words), len(words[0])
#         permutation_len = k * word_len

#         if permutation_len > n:
#             return []

#         counter = Counter(words)

#         def find_permutation(pos, offset):
#             if offset == permutation_len:
#                 return True

#             index = pos + offset
#             w = s[index:index + word_len]
#             if not counter[w]:
#                 return False

#             counter[w] -= 1
#             ret = find_permutation(pos, offset + word_len)
#             counter[w] += 1
#             return ret

#         seen = {}
#         output = []
#         for i in range(n - permutation_len + 1):
#             w = s[i:i+permutation_len]
#             if w not in seen:
#                 seen[w] = find_permutation(i, 0)
#             if seen[w]:
#                 output += [i]
#         return output


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        n = len(s)
        word_len = len(words[0])
        permu_len = word_len * len(words)

        times = Counter(words)

        output = []
        curr = Counter()

        def find_permutation(start_pos):
            pos = start_pos
            curr.clear()

            while start_pos + permu_len <= n:
                word = s[pos : pos + word_len]
                pos += word_len
                if word not in times:
                    start_pos = pos
                    curr.clear()
                else:
                    curr[word] += 1

                    while curr[word] > times[word]:
                        curr[s[start_pos : start_pos + word_len]] -= 1
                        start_pos += word_len
                    if pos - start_pos == permu_len:
                        output.append(start_pos)

        for i in range(min(word_len, n - permu_len + 1)):
            find_permutation(i)
        return output
