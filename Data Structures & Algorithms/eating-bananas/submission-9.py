import math
from typing import List

class Solution:
    def can_complete(self, k: int, piles: List[int], h: int) -> bool:
        time = 0

        for p in piles:
            time += math.ceil(p / k)

            if time > h:
                return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        answer = R

        while L <= R:
            K = (L + R) // 2

            if self.can_complete(K, piles, h):
                answer = K
                R = K - 1
            else:
                L = K + 1

        return answer