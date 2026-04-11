from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        L, R = 0, len(self.vals[key])-1
        res = ""
        stored = self.vals[key]
        while L <= R:
            M = (L+R) //2
            # if M is too small, its valid but look right
            if stored[M][1] < timestamp:
                res = stored[M][0]
                L = M+1
            elif stored[M][1] > timestamp:
                # look left M too big
                R = M - 1
            else:
                return stored[M][0]
        return res

        