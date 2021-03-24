def moveZerosToEnd(arr, n):  # Define function with parameters arr and len(arr)
    count = 0  # Count non-zero elements

    for i in range(n):
        if arr[i] != 0 and type(arr[i]) == int:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


arr = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
n = len(arr)
moveZerosToEnd(arr, n)
print(arr)
