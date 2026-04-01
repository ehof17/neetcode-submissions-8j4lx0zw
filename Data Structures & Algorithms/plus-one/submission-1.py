class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for val in reversed(digits):
            newVal = val + carry
            carry, newVal = divmod(newVal, 10)
            res.append(newVal)
        if carry:
            res.append(carry)
        return list(reversed(res))
