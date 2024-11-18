def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    arr[:] = arr[d:] + arr[:d]
    return arr 
arr = [1, 2, 3, 4, 5]
d = 2   
print(rotateArr(arr,d))


