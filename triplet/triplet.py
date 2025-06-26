# i < j < k
# nums[i] < nums[j] < nums[k]

class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
sol = Solution()
print(sol.increasingTriplet([5,4,3,2,1]))