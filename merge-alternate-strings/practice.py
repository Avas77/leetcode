class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        min_len = len(min(word1, word2, key=len))
        for index in range(min_len):
            merged += word1[index] + word2[index]
        if len(word1) == len(word2):
            return merged
        elif len(word1) == min_len:
            merged += word2[min_len:]
        else: 
            merged += word1[min_len:]
        return merged

sol = Solution()
print(sol.mergeAlternately('abcd', 'pq'))
        