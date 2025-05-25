# 0 means you can plant
# 1 means you cant plant
# you cannot pant flowers side by side

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for index, flower in enumerate(flowerbed):
            if flower:
                continue
            elif len(flowerbed) == 1 and flower == 0:
                return True 
            else:
                if n == 0:
                    break
                if index == 0 and not flowerbed[index + 1]:
                    flowerbed[index] = 1
                    n -= 1
                elif index == len(flowerbed) - 1 and not flowerbed[index-1]:
                    flowerbed[index] = 1
                    n -= 1
                elif not flowerbed[index-1] and not flowerbed[index + 1]:
                    flowerbed[index] = 1
                    n -= 1
                    print("Deducted", n)
                else:
                    continue
        if n:
            return False
        else: 
            return True
           


sol = Solution()
print(sol.canPlaceFlowers([0,0,1,0,0], 2))