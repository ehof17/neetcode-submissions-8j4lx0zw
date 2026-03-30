class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0

        # maxLeft
        # maxRight
        # minofThem
        # area = R - L
        # min(maxL, maxR) - curHeight
        # if negative, round up to 0

        res = 0
        maxLefts = [0] * len(height)
        maxRights = [0] * len(height)
        for i in range(1, len(height)):
            maxLefts[i] = max(height[i-1], maxLefts[i-1])
        for i in range(len(height)-2, -1, -1):
            maxRights[i] = max(height[i+1], maxRights[i+1])

        for i,h in enumerate(height):
            minVal = min(maxLefts[i], maxRights[i])
            valToUse = max(minVal - h, 0)
            res+=valToUse


        print(maxLefts)
        print(maxRights)
        return res