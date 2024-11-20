def majority_element_brute(arr):
    n = len(arr)
    result = []
    visited = []  

    for i in range(n):
        if arr[i] not in visited: 
            visited.append(arr[i])
            if arr.count(arr[i]) > n // 3:
                result.append(arr[i])

    return sorted(result)
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
print(majority_element_brute(arr)) # Output: [5, 6]
#TC --> O(n^2)
#SC --> O(n)
