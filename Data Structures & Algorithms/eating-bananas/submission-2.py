import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # rate = bananas per hour
        # divide
        # takes coco x * r 
        upper = max(piles)
        lower = 1
        if h == len(piles):
            return upper
        res = upper
        while lower <= upper:
            mid = (upper + lower) //2
            
            time_to_fin = 0
            for p in piles:
                time_to_fin+=math.ceil(float(p)/mid)
            
            
            if time_to_fin <= h:
                res = mid
                upper = mid -1
            else:
                lower = mid+1
            # if can finish
            # cut again
            # if can't finish
            # go right
            # can it finish at a rate of mid
       
        


        return res