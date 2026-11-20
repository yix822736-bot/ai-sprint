def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [7, 19, 23, 41, 58, 66, 79, 84, 93]
print(binary_search(nums, 66))
print(binary_search(nums, 50))
print(binary_search(nums, 7))
print(binary_search(nums, 93))
