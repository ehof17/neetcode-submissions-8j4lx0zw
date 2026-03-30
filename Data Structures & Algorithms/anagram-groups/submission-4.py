from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams into sublists
        # freq
        freqmap = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')]+=1
            freqmap[tuple(freq)].append(word)
        return list(freqmap.values())
