def moveZerosToEnd(arr, n):     # Define function with parameters arr and len(arr)
    count = 0  # Count non-zero elements

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


arr = [1, 9, 0, 5, 3, 4, 1, 0, 0, 3, 4]
n = len(arr)
moveZerosToEnd(arr, n)
print(arr)
