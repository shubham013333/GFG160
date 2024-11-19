def next_permutation_better(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = arr[i + 1:][::-1]
    return arr
arr = [1,2,3]
ans = next_permutation_better(arr)
print(ans)
#TC --> O(n)
#SC --> O(1)