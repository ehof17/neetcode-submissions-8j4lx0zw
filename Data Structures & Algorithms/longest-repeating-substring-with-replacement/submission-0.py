from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 0
        max_count = 0
        counts = defaultdict(int)
        for R in range(len(s)):
            counts[s[R]] += 1
            max_count = max(max_count, counts[s[R]])
            if (R - L + 1) - max_count > k:
                counts[s[L]] -= 1
                L+=1 
        return (R-L+1)