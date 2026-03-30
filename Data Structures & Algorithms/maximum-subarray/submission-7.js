class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */

    maxSubArray(nums) {
        let maxSum = nums[0]
        let curSum = 0

        for(let i = 0; i < nums.length; i++){
            curSum = curSum < 0 ? 0 : curSum
            curSum+=nums[i]
            maxSum = maxSum > curSum ? maxSum : curSum


        }
        return maxSum

    }
}
