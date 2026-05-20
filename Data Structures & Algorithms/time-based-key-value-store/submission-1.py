import bisect
class TimeMap:

    def __init__(self):
        self.time_kv: dict[str, list] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_kv:
            self.time_kv[key] = [(timestamp, value)]
        else:
            self.time_kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_kv:
            return ""
        vals = self.time_kv[key]
        idx = bisect.bisect_right(vals, (timestamp, chr(255))) - 1
        return vals[idx][1] if idx >= 0 else ""