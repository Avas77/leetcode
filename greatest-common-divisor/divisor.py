class Solution:
    def gcdOfStrings(self, str1, str2):
        base = str1 if len(str1) < len(str2) else str2
        
        for i in range(len(base), 0, -1):
            candidate = base[:i]
            
            # Check if both strings can be formed by repeating the candidate
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                if str1 == candidate * (len(str1) // len(candidate)) and \
                str2 == candidate * (len(str2) // len(candidate)):
                    return candidate
        
        return ""

sol = Solution()
print(sol.gcdOfStrings("ABCABCABC", "ABCA"))