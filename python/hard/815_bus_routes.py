from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        stop_bus_map = defaultdict(list)

        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_bus_map[stop] += [bus]

        q = deque(stop_bus_map[source])
        visited_stop = {source}
        visited_bus = set(stop_bus_map[source])
        transfers = 1
        while q:
            level_size = len(q)
            for _ in range(level_size):

                bus = q.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return transfers

                    if stop in visited_stop:
                        continue
                    
                    visited_stop.add(stop)
                    for next_bus in stop_bus_map[stop]:
                        if next_bus not in visited_bus:
                             visited_bus.add(next_bus)
                             q += [next_bus]
                    
            transfers += 1
        return -1