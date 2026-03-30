class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for word in strs:
            char_cnt = [0] * 26
            for char in word:
                char_cnt[ord(char)-ord('a')]+=1
            char_tup = tuple(char_cnt)
            if char_tup in res_dict:
                res_dict[char_tup].append(word)
            else:
                res_dict[char_tup] = [word]
        
        return list(res_dict.values())