#Brute Force Approach (O(n log n))
def second_largest_brute(arr):
    arr = list(set(arr))
    if len(arr) < 2:
        return -1
    arr.sort()
    return arr[-2]

# Example Usage
print(second_largest_brute([12, 35, 1, 10, 34, 1]))  # Output: 34
print(second_largest_brute([10, 5, 10]))  # Output: 5
print(second_largest_brute([10, 10, 10]))  # Output: -1
