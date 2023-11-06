class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        n = len(arr)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            ts, val = arr[mid]
            if ts <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        return "" if lo == 0 else arr[lo - 1][1]

        # i = bisect.bisect(self.data[key], (timestamp, chr(127)))
        # return "" if i == 0 else self.data[key][i - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
