# 1. 变量
name = "小燚"
print(name)
print("我是" + name)

# 2. 循环：1-100 奇数和
total_odd = 0
for i in range(1, 101):
    if i % 2 == 1:
        total_odd = total_odd + i
print(total_odd)

# 3. 函数
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

# 4. 列表
def sum_list(nums):
    total = 0
    for n in nums:
        total = total + n
    return total

print(sum_list([3, 4, 9, 8, 2, 6, 7]))

def find_max(nums):
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest

print(find_max([3, 4, 9, 8, 2, 6, 7]))

# 5. 字典：统计 hello
counts = {}
for ch in "hello":
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
print(counts)
