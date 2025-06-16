# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

class Solution(object):
    def compress(self, chars):
        s = ""
        count_char = dict()
        for char in chars:
            if char not in count_char:
                count_char[char] = 1
            else:
                count_char[char] += 1
        for item, value in count_char.items():
            if value == 1:
                s += item
            else:
                s = s + item + str(value)
        return [char for char in s]

sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
            
        