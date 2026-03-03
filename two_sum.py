def two_sum(nums, target):
    nums_with_index = sorted([(num, i) for i, num in enumerate(nums)])
    
    left = 0
    right = len(nums_with_index) - 1
    
    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        
        if current_sum == target:
            return [
                nums_with_index[left][1],
                nums_with_index[right][1]
            ]
        elif current_sum < target:
            left += 1
        else:
            right -= 1