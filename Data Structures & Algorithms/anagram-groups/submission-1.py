from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams into sublists
        # freq
        freqMap = defaultdict(list)
        for word in strs:
            freqs = [0] * 26
            for char in word:
                freqs[ord(char)-97]+=1
            freqMap[tuple(freqs)].append(word)
        res = []
        for words in freqMap.values():
            res.append(words)
        return res
        
            
        
        