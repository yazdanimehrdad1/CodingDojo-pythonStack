def bubble_sort(arr):

    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i+1] <arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


testArr = [6,3,0,2,4,9,5,1]
result = bubble_sort(testArr)
print(result)