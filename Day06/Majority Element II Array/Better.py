def majority_element_better(arr):
    n = len(arr)
    dic = {}
    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    result = []
    for key, value in dic.items():
        if value > n // 3:
            result.append(key)
    return sorted(result)
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
print(majority_element_better(arr))  # Output: [5, 6]
#TC --> O(n)
#SC --> O(n)


