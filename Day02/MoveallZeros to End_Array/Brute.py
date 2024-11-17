#Brute Force Approach (O(n) space, O(n) time)
def move_zeros_brute(arr):
    non_zero = [x for x in arr if x != 0]
    zero_count = len(arr) - len(non_zero)
    arr[:] = non_zero + [0] * zero_count
    return arr

print(move_zeros_brute([1, 2, 0, 4, 3, 0, 5, 0]))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
print(move_zeros_brute([10, 20, 30]))  # Output: [10, 20, 30]
print(move_zeros_brute([0, 0]))  # Output: [0, 0]
