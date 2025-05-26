class Solution:
    def reverseVowels(self, s: str) -> str:
        if type(s) != str:
            return
        vowels = ['a', 'e', 'i', 'o', 'u']
        char_order = dict()
        for index, char in enumerate(s.lower()):
            if char in vowels:
                char_order[index] = s[index]
        key_char = list(char_order.keys())
        values_char = list(char_order.values())
        reverse_char = values_char[::-1]
        result = dict(zip(key_char, reverse_char))
        rev_char = list(s)
        for key, val in result.items():
            rev_char[key] = val
        return "".join(rev_char)

sol = Solution()
print(sol.reverseVowels("IceCreAm"))