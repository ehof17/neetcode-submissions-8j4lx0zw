class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            word_cnt = len(word)
            res+=str(word_cnt)
            res+="#"
            res+=word
        print(res)
        return res
  
        
       

    def decode(self, s: str) -> List[str]:
        res = []
        prev_word_idx = 0
        L = 0
        while L < len(s):
            if s[L] == "#":
                # at this point we can ge the num
                number = int(s[prev_word_idx:L])
                new_word = (s[L+1:L+1+number])
                res.append(new_word)
                prev_word_idx = L+number+1
                L = L+1+number
            else:
                L+=1
        return res





                

       


       