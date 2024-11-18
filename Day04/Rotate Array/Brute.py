def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    for _ in range(d):
        temp = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[-1] = temp
    return arr
arr = [1, 2, 3, 4, 5]
d = 2   
print(rotateArr(arr,d))