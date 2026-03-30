class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict
        # cnt of each val is the key
        # value is a list of the letters
        resDict = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')]+=1
            key = tuple(count)
            if key not in resDict:
                resDict[key] = []
            
            # Append the word
            resDict[key].append(word)
        return list(resDict.values())