class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for L in range(len(nums)):
            for R in range(L + 1, min(len(nums), L + k + 1)):
                if nums[L] == nums[R]:
                    return True
        return False