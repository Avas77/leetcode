class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found_list = list()
        for char1 in s:
            for index, char2 in enumerate(t):
                if char1 == char2:
                    found_list.append(index)
        print(found_list)
        if found_list:
            left = found_list[0]
            for index in found_list:
                if left <= index:
                    left = index
                else: 
                    return False
            return True
        else:
            return False
            

sol = Solution()
print(sol.isSubsequence("axc", "ahbgdc")) 