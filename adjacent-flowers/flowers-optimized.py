class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for index in range(len(flowerbed)):
            if flowerbed[index] == 0:
                empty_left = (index == 0) or (flowerbed[index - 1] == 0)
                empty_right = (index == len(flowerbed) - 1) or (flowerbed[index + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[index] = 1
                    count += 1
        return count >= n 


sol = Solution()
print(sol.canPlaceFlowers([1, 0, 1], 1))
                

        