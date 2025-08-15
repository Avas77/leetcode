def max_list(nums):
    output = [None] * len(nums)
    left = None
    for i in range(len(nums)):
        if not left:
            left = nums[i]
        else: 
            output[i] = left 
            left = max(left, nums[i])

    right = None
    for i in range(len(nums) - 1, -1, -1):
        if not right:
            right = nums[i]
        else:
            if output[i]:
                output[i] = max(output[i], right)
                right = max(right, nums[i])
            else:
                output[i] = right
    return output

    
max_list([1,2,3,4])

[4,4,4,3]