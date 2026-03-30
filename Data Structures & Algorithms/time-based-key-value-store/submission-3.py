from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.vals.get(key)
        if not vals:
            return ""
        L, R = 0, len(vals)-1
        res = ""
        while L <= R:
            M = (L+R) // 2
            v,t = vals[M]
            if t <= timestamp:
                res = v
                L = M + 1
            else:
                R = M - 1
        return res
