from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.maps.get(key)
        if not vals:
            return ""
        L = 0
        R = len(vals) - 1
        res = ""
        while L <= R:
            mid = (R+L) //2
            val, times = vals[mid]
            if times <= timestamp:
                res = val
                L = mid +1
            else:
                R = mid -1
        return res
            


        
