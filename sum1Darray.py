class Solution:
    def runningSum(self, nums):
        n = len(nums)
        if n < 2:
            return nums
        rSum = [0] * n
        rSum[0] = nums[0]
        for i in range(1, n):
            rSum[i] = nums[i] + rSum[i - 1]
        return rSum

