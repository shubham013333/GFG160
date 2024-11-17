#Better Approach (O(2n))
def second_largest_better(arr):
    largest = max(arr)
    filtered = [x for x in arr if x != largest]
    return max(filtered) if filtered else -1

# Example Usage
print(second_largest_better([12, 35, 1, 10, 34, 1]))  # Output: 34
print(second_largest_better([10, 5, 10]))  # Output: 5
print(second_largest_better([10, 10, 10]))  # Output: -1
