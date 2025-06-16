class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_str = max(word1, word2, key=len)
        merge_string = []
        for index in range(len(max_str)):
            if index < len(word1) and index < len(word2):
                merge_string.append(word1[index]) 
                merge_string.append(word2[index])
            else:
                merge_string.append(max_str[index])
        return "".join(merge_string)

sol = Solution()
print(sol.mergeAlternately('abcd', 'pq'))
        