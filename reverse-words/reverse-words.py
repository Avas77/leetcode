class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.strip()
        words = text.split(" ")
        reverse_list = [word for word in reversed(words) if word]
        return ' '.join(reverse_list)
    
sol = Solution()
print(sol.reverseWords(" Hello World "))