def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i
    return []

print(two_sum([8, 3, 11, 5, 2], 14))
print(two_sum([13, 6, 1, 9], 10))
