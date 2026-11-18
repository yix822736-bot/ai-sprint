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

def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] !=0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow+=1
    return nums
print(move_zeroes([0, 7, 0, 3, 12, 0, 5]))

def contains_duplicate(nums):
    seen=set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False
print(contains_duplicate([17, 4, 29, 8, 4]))         
print(contains_duplicate([31, 7, 19, 42]))

