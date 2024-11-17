#Using Two Pointers (In-Place, O(n))
def reverse_array_two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_array_two_pointers([1, 4, 3, 2, 6, 5]))  # Output: [5, 6, 2, 3, 4, 1]

