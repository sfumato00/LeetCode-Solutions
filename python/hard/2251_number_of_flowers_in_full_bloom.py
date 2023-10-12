from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        events = []
        for s, e in flowers:
            events += [(s, 1)]
            events += [(e + 1, -1)]

        events.sort(key=lambda x: (x[0], x[1]))
        sorted_people = sorted(set(people))
        n = len(events)
        dic = {}
        count = 0
        i = 0
        for p in sorted_people:
            while i < n and events[i][0] <= p:
                count += events[i][1]
                i += 1
            dic[p] = count
        return [dic[p] for p in people]
