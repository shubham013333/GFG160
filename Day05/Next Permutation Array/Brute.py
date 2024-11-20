from itertools import permutations
def next_permutation_brute(arr):
    perms = sorted(permutations(arr))
    for i in range(len(perms)):
        if list(perms[i]) == arr:
            return list(perms[i + 1]) if i + 1 < len(perms) else list(perms[0])
arr = [1,2,3]
ans = next_permutation_brute(arr)
print(ans) #Output --> [1, 3, 2]
#TC --> O(n!⋅n)
#SC --> O(n!⋅n)