class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # inp is 7
        # chunk size is 3
        # end up with 5 chunks
        # since 7-3 = 4

        chunks = len(nums) - k + 1
        for i in range(chunks):       
            chunk2 = nums[i:i+k]
            chunk_max = max(chunk2)
            res.append(chunk_max)
        return res