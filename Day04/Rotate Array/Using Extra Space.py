def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    temp = arr[:d]
    for i in range(n - d):
        arr[i] = arr[i + d]
    arr[n - d:] = temp
    return arr

arr = [1, 2, 3, 4, 5]
d = 2   
print(rotateArr(arr,d))

