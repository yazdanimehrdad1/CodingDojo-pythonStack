

def selectionSort(arr):
    for i in range(0, len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[j]< arr[minIdx]:
                arr[minIdx], arr[j] = arr[j], arr[minIdx]
    return arr

testArr = [8, 5, 2, 9, 5, 6, 3,0]
print(selectionSort(testArr))