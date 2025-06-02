class Solution:
    def product(self, nums):
        prod = 1
        for num in nums:
            prod *= num
        return prod
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        newArr = []
        for index in range(len(nums)):
            dupArr = nums.copy()
            del dupArr[index]
            newArr.append(self.product(dupArr))
        print(newArr)

sol = Solution()
sol.productExceptSelf([-1,1,0,-3,3])