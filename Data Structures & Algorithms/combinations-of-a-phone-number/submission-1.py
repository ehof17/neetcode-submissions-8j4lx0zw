numToChars = {"2": ['a','b', 'c'],
 "3":['d','e', 'f'],
  "4": ['g','h','i'],
  "5": ['j', 'k', 'l'],
  "6": ['m', 'n', 'o'],
  "7": ['p', 'q', 'r', 's'],
  "8": ['t', 'u', 'v'],
  "9": ['w', 'x', 'y', 'z'],}



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        k = len(digits)
        if k == 0:
            return []

        def helper(i, curSet, resSet):
            if i >= len(digits):
                resSet.append("".join(curSet))
                return
            digit = digits[i]
            new_digits = numToChars.get(digit)
            for digit in new_digits:
                curSet.append(digit)
                helper(i+1, curSet, resSet)
                curSet.pop()
            
        
    
        resSet = []
        helper(0, [], resSet)
        print(resSet)
        return resSet


        