#selection sort
def find(arr):
    minim = arr[0]
    minim_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < minim:
            minim = arr[i]
            minim_ind = i
    return minim_ind

def selSort(arr):
    newArr = []
    for i in range(len(arr)):
        minim = find(arr)
        newArr.append(arr.pop(minim))
    return newArr

print(selSort([5,3,6,2,10]))
