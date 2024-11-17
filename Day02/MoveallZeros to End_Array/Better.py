#Better Approach (Two Pointers, O(n) time, O(1) space)
def move_zeros_better(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    return arr

print(move_zeros_better([1, 2, 0, 4, 3, 0, 5, 0]))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros_better([10, 20, 30]))  # Output: [10, 20, 30]
print(move_zeros_better([0, 0]))  # Output: [0, 0]
