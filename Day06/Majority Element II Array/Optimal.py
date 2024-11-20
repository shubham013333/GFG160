#Boyer-Moore Voting Algorithm
def majority_element_optimal(arr): 
    n = len(arr)
    first, second, count1, count2 = None, None, 0, 0

    for num in arr:
        if num == first:
            count1 += 1
        elif num == second:
            count2 += 1
        elif count1 == 0:
            first, count1 = num, 1
        elif count2 == 0:
            second, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    for candidate in [first, second]:
        if arr.count(candidate) > n // 3:
            result.append(candidate)

    return sorted(result)
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
print(majority_element_optimal(arr))  # Output: [5, 6]
#TC --> O(n)
#SC --> O(1)

