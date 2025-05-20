# candies as integer array and extraCandies as integer
# result booleam array such that if i give candy to a kid the kid must have the highest number of candies

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        largest = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= largest)
        return result

sol = Solution()
print(sol.kidsWithCandies([4,2,1,1,2], 1))