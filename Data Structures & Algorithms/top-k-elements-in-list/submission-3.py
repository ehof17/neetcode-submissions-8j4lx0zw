class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        freq = [[] for i in range(len(nums)+1)]

        for key,v in counts.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
                

 

        





        