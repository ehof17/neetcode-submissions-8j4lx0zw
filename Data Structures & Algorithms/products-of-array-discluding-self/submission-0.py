class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # go thru setting the value to the prev val
        #
        curProd = 1
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i + 1]
            prefix[i] *= postfix[i]

            
        print(postfix)
        return prefix
