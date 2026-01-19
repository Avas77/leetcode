def kadanes_with_subarray(nums):
    global_max = nums[0]
    current_max = nums[0]
    
    start = 0
    best_start = 0
    best_end = 0
    
    for i in range(1, len(nums)):
        # Decide: Start a new subarray or extend the current one?
        if nums[i] > current_max + nums[i]:
            current_max = nums[i]
            start = i 
        else:
            current_max += nums[i]
        
        # Update the global best and its coordinates
        if current_max > global_max:
            global_max = current_max
            best_start = start
            best_end = i
            
    return nums[best_start : best_end + 1], global_max

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray, max_sum = kadanes_with_subarray(arr)
print(f"Subarray: {subarray}, Sum: {max_sum}")
# Output: Subarray: [4, -1, 2, 1], Sum: 6