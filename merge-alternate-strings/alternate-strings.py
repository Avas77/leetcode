# two strings: word1 and word 2
# merge strings but in alternating order
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# return merged string
# # Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

def merge_alternate(word1: str, word2: str) -> str:
    merged = list()
    value = 0
    sliced = ''
    if len(word1) > len(word2):
        value = len(word2)
        sliced = word1[len(word2):]
    elif len(word1) < len(word2):
        value = len(word1)
        sliced = word2[len(word1):]
    else:
        value = len(word1)

    for i in range(value):
        merged.append(word1[i] + word2[i])
    merged.append(sliced)
    return ''.join(merged)
    

print(merge_alternate('abc', 'pqr'))