class Solution(object):
    def moveZeroes(self, nums):
        zero_index = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                zero_index += 1
        return nums

sol = Solution()
sol.moveZeroes([0,1])