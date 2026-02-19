class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        unique_set = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                unique_set.remove(nums[L])
                L += 1
            if nums[R] in unique_set:
                return True
            unique_set.add(nums[R])
        return False