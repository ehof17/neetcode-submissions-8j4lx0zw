class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += (s)
        return res
        
       

    def decode(self, s: str) -> List[str]:
        res = []
        # check where # starts
        # then slice to next #
        i = 0
        startNum = 0
        # scan for length of string
        while i < len(s):
            if s[i] == "#":
                # number is from start to i
                numberStr = s[startNum:i]
                # length of word to add
                lengthInt = int(numberStr)
                wordToAdd = s[i+1:i+lengthInt+1]
                print('we are about to add', wordToAdd)
                res.append(wordToAdd)
                startNum = i + lengthInt+1
                i = startNum


            i+=1
       
        return res
                

       


       