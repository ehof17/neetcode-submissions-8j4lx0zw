from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = defaultdict(int)
        tCount = defaultdict(int)
        for cs in s:
            sCount[cs]+=1
        for ct in t:
            tCount[ct]+=1
        return sCount == tCount

