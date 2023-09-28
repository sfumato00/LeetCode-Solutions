class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # concise
        # ch_to_index = defaultdict(lambda: 26)
        # return "".join(sorted(s, key=lambda c:ch_to_index[c]))

        # bucket sort
        rank = [i for i in range(26)]
        ch_to_index = defaultdict(lambda: 26)
        for i, ch in enumerate(order):
            ch_to_index[ch] = i
        bucket = [0] * 26
        output = []
        for ch in s:
            if ch in ch_to_index:
                bucket[ch_to_index[ch]] += 1
            else:
                output += [ch]

        for i, freq in enumerate(bucket):
            if freq > 0:
                output += [order[i] * freq]
        return "".join(output)
