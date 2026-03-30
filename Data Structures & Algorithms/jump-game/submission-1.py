class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # go as far as we can
        # then go less
        goal = len(nums) -1
        # keep moving the goal back
        for i in range(len(nums) -2, -1, -1):
            print(f"Goal is {goal}")
            # can reach from i
            if i + nums[i] >= goal:
            # move goal to 
                goal = i


        if goal == 0:
            return True

        return False
