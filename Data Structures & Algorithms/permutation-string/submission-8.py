from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = defaultdict(int)
        for c in s1:
            cnt_s1[c]+=1

        # now go thru S2
        # if all chars are valid
        # meaning that when we get to the char
        # and the cnt_s1 is not null and cnt_s1[char] > 0

        # update cnt_s1
        # Then, if all cnt_s1 is 0, return true
        L = 0
        # if our window ever gets too big, we need to start re adding to cnt_s1
        for R in range(len(s2)):
            chr_r = s2[R]
            # we have the char and the cnt of it is greater than 0
            if cnt_s1[chr_r] > 0:
                cnt_s1[chr_r]-=1
           
            else:
                # we either don't have the char, or the cnt of it is 0
                # move the left pointer
                while L <= R and s2[L] != chr_r:
                    chr_L = s2[L]
                    # if it was in the previous window
                    # add it back
                    if chr_L in cnt_s1:
                        cnt_s1[chr_L]+=1
                    L+=1
                # move the window
                L+=1
            if R - L + 1 == len(s1):
                return True
        return False