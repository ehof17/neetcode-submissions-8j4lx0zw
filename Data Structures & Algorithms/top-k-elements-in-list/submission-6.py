class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts of num -> occurences
        counts = {}
        for num in nums:
            counts[num] = 1+counts.get(num, 0)
         
        # occurences to number
        occur_to_list= [[] for i in range(len(nums)+1)]
        for key, val in counts.items():
            occur_to_list[val].append(key)
          
        res = []
        for i in range(len(occur_to_list)-1, -1, -1):
            vals = occur_to_list[i]
            for val in vals:
                res.append(val)
                if len(res) == k:
                    return res

        
                
            

                

 

        





        