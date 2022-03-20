class Solution:
    def solve(self, nums):

        if sum(nums)-nums[0] == 0:
            return 0

        prefix, suffix = 0, sum(nums)

        for i in range(len(nums)):
            suffix -= nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]
        return -1
