from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        charMap = defaultdict(int)

        # expand it as long as we can as the condition is valid
        # as soon as its not valid, shift left
        #
        for c in charSet:
            count = L = 0
            for R in range(len(s)):
                if s[R] == c:
                    count+=1

                # not valid
                while (R-L+1) - count > k:
                    # remove from window
                    if s[L] == c:
                        count-=1
                    L+=1
                res = max(res, R-L+1)
        return res
            
        # iterate through
        # if we find something not matching, then
        # remove one from gap
        # maximize the substring
        
        # we want to replace the less frequently inputted character
        # all characters in a window to match the

        # map -> character -> count
        # ABABBA
        # A:1
        # B:3
        # how is this window valid?
        # BABB
        # count of most frequent character
        # Take Len - count[B]
        # 4 - 3 = 1
        # 1 is the number of characters in our window
        # that do not match the most common character
        # if its less than or equal to k, we can update the pointer


