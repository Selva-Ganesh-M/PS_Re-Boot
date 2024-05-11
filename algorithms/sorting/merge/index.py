def merge_sort(arr: list[int]):
    if (len(arr)==1): 
        return arr
    mid = len(arr)//2
    leftHalf = merge_sort(arr[:mid])
    rightHalf = merge_sort(arr[mid:])
    ansArr = []
    i=j=0
    while(i<len(leftHalf) and j<len(rightHalf)):
        if leftHalf[i]<rightHalf[j]:
            ansArr.append(leftHalf[i])
            i+=1
        else:
            ansArr.append(rightHalf[j])
            j+=1
    ansArr.extend(leftHalf[i:])
    ansArr.extend(rightHalf[j:])
    return ansArr

lis = [5,4,3,2, 11,1]
print(merge_sort(lis))