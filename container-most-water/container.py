class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            if maxArea < area:
                maxArea = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        
            
sol = Solution()
print(sol.maxArea([1,1]))