class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        first = 0
        last = len(nums) - 1
        count = 0
        while first < last:
            sum = nums[first] + nums[last]
            if sum == k:
                count += 1
                first += 1
                last -= 1
            elif sum < k:
                first += 1
            else:
                last -= 1
        return count

sol = Solution()
print(sol.maxOperations([3,1,3,4,3], 6))