def sum_array(nums):
    output = [0] * len(nums)
    left = 0
    for i in range(len(nums)):
        output[i] += left
        left += nums[i]
    right = 0
    for i in range(len(nums) - 1, -1, -1):
        output[i] += right
        right += nums[i]
    print(output)
    return output

sum_array([4, 5, 1, 2])