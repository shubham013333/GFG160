#Optimal Approach (O(n))
def second_largest_optimal(arr):
    largest = second = -1
    for num in arr:
        if num > largest:
            second, largest = largest, num
        elif num > second and num != largest:
            second = num
    return second

# Example Usage
print(second_largest_optimal([12, 35, 1, 10, 34, 1]))  # Output: 34
print(second_largest_optimal([10, 5, 10]))  # Output: 5
print(second_largest_optimal([10, 10, 10]))  # Output: -1
