from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams into sublists
        # freq
        freqMap = defaultdict(list)
        for word in strs:
            freqs = [0]*26
            for char in word:
                idx = ord(char) - 97
                freqs[idx] +=1
            freqMap[tuple(freqs)].append(word)

        res = []
        for vals in freqMap.values():
            res.append(vals)
        return res
        
            
        
        