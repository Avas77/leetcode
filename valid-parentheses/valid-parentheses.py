class Solution(object):
    def isValid(self, s):
        stack = []
        valid_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char == "(" or char == "{" or char == "[":
              stack.append(char)
            elif char in valid_map.keys() and valid_map[char] == stack[-1]:
              stack.pop()
            else:
              continue
        return len(stack) == 0

sol = Solution()
print(sol.isValid('{ "data": [ { "id": 1 } '))