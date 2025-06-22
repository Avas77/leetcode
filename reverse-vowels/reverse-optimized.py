class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "U"]
        vowels_found = list()
        reversed = list()
        for char in s:
            if char in vowels:
                vowels_found.append(char)
        for char in s:
            if char in vowels:
                reversed.append(vowels_found.pop())
            else:
                reversed.append(char)
        return "".join(reversed)
        
        
sol = Solution()
print(sol.reverseVowels("leetcode"))