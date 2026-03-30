class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n
        while True:
            val = 0
            for digit in str(number):
                dig = int(digit)
                val+= dig **2
            if val == 1:
                return True
            if val in seen:
                return False
            seen.add(val)
            number = val
        