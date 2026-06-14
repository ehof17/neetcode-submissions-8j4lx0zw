from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # XYYX
        # ^
        # ^
        # replacements left: 2
        # XYYX
        # ^^ replacements left: 1, len 2
        #
        # XYYX
        # ^ ^ replacements left: 0, len 3
        # XYYX
        # ^  ^ replacements left 0, len 4

        #then do we gotta move next?

        # XYYX
        #  ^

        # AAABABB
        # ^ replacements left 1, len 4
        # ^ 
        # ^    ^ replacements left 0, but need to replace
        # ^    ^
        # until we get to a DIFFERENT THing
        # AAABABB
        #    ^ replacements left 1
        #.   ^^ replacements left 0, len 1
        #    ^ ^ Gotta shrink til we get to a different thing
        #.     ^

        # idea: count num of chars
        # if the window length
        # if max(count of the same Char) + k >= window length
        # then the window is valid
        # If we encounter a thing where its invalid
        # then we gotta start removing from our left pinter
        maxLen = 0
        char_cnts = defaultdict(int)
        L,R=0,0
        for R in range(len(s)):
            char_cnts[s[R]] += 1
            window_len = R - L + 1
            max_char_cnt = max(char_cnts.values())
            if max_char_cnt + k >= window_len:
                maxLen = max(maxLen, window_len)
            else: 
                char_cnts[s[L]] -= 1
                L += 1
        return maxLen