import heapq
from typing import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        heap = [(-freq, ch) for ch, freq in cnt.items()]
        heapq.heapify(heap)
        output = []
        while heap:
            if output and heap[0][1] == output[-1]:
                return ""
            freq, ch = heapq.heappop(heap)
            freq = -freq - 1
            output.append(ch)

            if heap:
                freq2, ch2 = heapq.heappop(heap)
                freq2 = -freq2 - 1
                output.append(ch2)
                if freq2 > 0:
                    heapq.heappush(heap, (-freq2, ch2))
            if freq > 0:
                heapq.heappush(heap, (-freq, ch))
        return "".join(output)
