#Example:
# Input: [4, 2, 7, 1]
# Output: [1, 1, 0, 0]]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    count += 1
            result.append(count)
        print(result)

sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])