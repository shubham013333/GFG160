#Optimal Approach (O(n) time, O(1) space)
def move_zeros_optimal(arr):
    index = 0
    for num in arr:
        if num != 0:
            arr[index] = num
            index += 1
    for i in range(index, len(arr)):
        arr[i] = 0
    return arr

print(move_zeros_optimal([1, 2, 0, 4, 3, 0, 5, 0]))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros_optimal([10, 20, 30]))  # Output: [10, 20, 30]
print(move_zeros_optimal([0, 0]))  # Output: [0, 0]
