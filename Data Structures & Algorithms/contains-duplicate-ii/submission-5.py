class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(k==0):
            return False
    
        numSet = set()
        begin = 0
        end = k
        numSet = set([i for i in nums[:k]])
        if len(numSet) < k:
            return True
        for num in nums[k:]:
            if num in numSet:
                return True
            numSet.remove(nums[begin])
            numSet.add(nums[end])
            begin+=1
            end+=1
        return False
        print(numset)
        print(f"k is {k}")
        print(f"nums at end is {nums[end]}")
        print(f" len of numset is {len(numset)}")
        if (len(numset)<=k):
            return True

        numset.remove(nums[begin])
        begin+=1

        numset.add(nums[end])
        end+=1
        if (len(numset) <k):
            return True

        return False


 

            
        