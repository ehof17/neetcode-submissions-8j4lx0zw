class Solution:
    def trap(self, height: List[int]) -> int:
        # at a given place
        # height at a given val is min(maxRight, maxLeft) - currHeight
        maxLefts =[0]*len(height)
        for i,h in enumerate(height):
            if i <= 0:
                continue
            maxLefts[i] = max(maxLefts[i-1], height[i-1])
        maxRights = [0]*len(height)
        for i in range(len(height), -1, -1):
            if i >= len(height)-1: continue
            maxRights[i] = max(maxRights[i+1], height[i+1])
        
        total_watuh = 0
        for i, h in enumerate(height):
            max_left = maxLefts[i]
            max_right = maxRights[i]
            val_to_use = max_left if max_left < max_right else max_right
            watuh = max(0, val_to_use - h)
            total_watuh+=watuh
            
        return total_watuh