class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = [len(x) for x in strs]
        print(lens)
        res = ""
        for i in range(len(strs)):
            
            res += str(lens[i])
            res +="#"
            res += strs[i]
            
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        L = 0
        while L < len(s):
            lengthstr = ""
            curr = L
            while s[curr] != "#":
                lengthstr += s[curr]
                curr+=1

            
            length = int(lengthstr)
            base = curr+1
            word= s[base:length+base]
            print(f"found Word {word}")
            res.append(word)
            L = length + base
        return res
