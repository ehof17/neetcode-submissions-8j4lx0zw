numToChars = {"2": ['a','b', 'c'],
 "3":['d','e', 'f'],
  "4": ['g','h','i'],
  "5": ['j', 'k', 'l'],
  "6": ['m', 'n', 'o'],
  "7": ['p', 'q', 'r', 's'],
  "8": ['t', 'u', 'v'],
  "9": ['w', 'x', 'y', 'z'],}




        

    # try everything at current Char


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        k = len(digits)
        if k == 0:
            return []

        def helper(i, curSet, resSet):
            if len(curSet) == k:
                print(curSet)
                resSet.append("".join(curSet.copy()))
                return
            if i > k:
                return
            
            cur = digits[i]
            vals = numToChars.get(cur)
            for val in vals:
                curSet.append(val)
                helper(i+1, curSet, resSet)
                curSet.pop()
            
    
        resSet = []
        helper(0, [], resSet)
        return resSet


        