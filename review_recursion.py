def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])


print(sum_list([13, 27, 8, 41]))
