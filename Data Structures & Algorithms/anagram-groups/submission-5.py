class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countDict = {}
        for string in strs:
            counts = {i:0 for i in range(26)}
            for c in string:
                counts[ord(c)-ord('a')] +=1
            countKey = tuple(counts.values())
            if countDict.get(countKey):
                countDict[countKey].append(string)
            else:
                countDict[countKey] = [string]
        return list(countDict.values())