class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0

        # maxLeft
        # maxRight
        # minofThem
        # area = R - L
        # min(maxL, maxR) - curHeight
        # if negative, round up to 0

        maxLefts = [0] * len(height)
        maxRights = [0] * len(height)
        for i in range(1, len(height)):
            maxLefts[i] = max(maxLefts[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            maxRights[i] = max(maxRights[i+1], height[i+1])
        res = 0
        for i, h in enumerate(height):
            curHeight = min(maxLefts[i], maxRights[i]) - h
            curHeight = max(curHeight, 0)
            res+=curHeight
        return res

