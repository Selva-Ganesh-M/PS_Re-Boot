def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if (not swapped): break
    return arr

arr = [5,4,3, 9, 0, 11]
print(bubble_sort(arr))