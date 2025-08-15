#Example:
# Input: [4, 2, 7, 1]
# Output: [1, 1, 0, 0]]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)

        #Left Pass: Get the products of the every element on the left of the current index element
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        #Right Pass: Multiply the left products with the right element from the current position
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output
        
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))