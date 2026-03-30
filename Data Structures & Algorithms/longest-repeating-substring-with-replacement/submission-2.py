from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # Valid if len ( R- L + 1) - maxF <= k
        L = 0
        counts = defaultdict(int)
        max_c = 0
        length = 0
        for R in range(len(s)):
            # Expand til we are invalid
            # L stays same
            counts[s[R]]+=1
            max_c = max(max_c, counts[s[R]])
            # Then shrink that thing
            if (R - L + 1) - max_c > k:
                counts[s[L]]-=1
                L+=1
        return (R-L+1)



