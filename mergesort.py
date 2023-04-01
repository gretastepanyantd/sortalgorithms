# Merge Sort-n*logn

data = [8, 5, 2, 7, 6, 4, 1, 3]
data1 = [2, 5, 7, 8]
data2 = [1, 3, 4, 6]


def sort(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    return result


def devide(data):
    if len(data) < 2:
        return data
    else:
        middle = len(data) // 2
        arr1 = devide(data[0:middle])
        arr2 = devide(data[middle:])
        return sort(arr1, arr2)


print(devide(data))
