class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the occurences

        cnt_map = {}
        for num in nums:
            if num in cnt_map:
                cnt_map[num]+=1
            else:
                cnt_map[num]=1
        
        # key is num, val is cnt
        # group these into new dict
        # Grab the keys in descending order of Val
        # at most num distinct numbers
        # 
        new_cnts = [[] for _ in range(len(nums)+1)]

        for num, occurences in cnt_map.items():
            new_cnts[occurences].append(num)
        res = []
  
        for i, e in reversed(list(enumerate(new_cnts))):
            if new_cnts[i]:
                for val in new_cnts[i]:
                    res.append(val)
                    if len(res) == k:
                        return res




        
                
            

                

 

        





        