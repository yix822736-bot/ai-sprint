#冒泡
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] >arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
        print(arr)        
    return arr

bubble_sort([9, 4, 6, 2])
#二分
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([2, 4, 6, 9], 6))
print(binary_search([2, 4, 6, 9], 5))


arr2 = [7, 3, 8, 1, 5]
bubble_sort(arr2)
print(binary_search(arr2, 8))
