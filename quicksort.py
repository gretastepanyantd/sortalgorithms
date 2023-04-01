# Quick Sort-n*logn

data = [4, 5, 1, 3, 7, 2, 6, 8]


def get_pivot(data, l, r):
    middleindex = (l + r) // 2
    if (data[l] >= data[r] and data[l] <= data[middleindex]) or (data[l] <= data[r] and data[l] >= data[middleindex]):
        pivotindex = l
    elif (data[r] >= data[l] and data[r] <= data[middleindex]) or (data[r] <= data[l] and data[r] >= data[middleindex]):
        pivotindex = r
    elif (data[middleindex] >= data[l] and data[middleindex] <= data[r]) or (
            data[middleindex] <= data[l] and data[middleindex] >= data[r]):
        pivotindex = middleindex
    return pivotindex


def sort(data, l, r):
    pivotindex = get_pivot(data, l, r)
    pivotvalue = data[pivotindex]
    data[l], data[pivotindex] = data[pivotindex], data[l]
    border = l
    for i in range(l, r + 1):
        if data[i] < pivotvalue:
            border += 1
            data[border], data[i] = data[i], data[border]
    data[l], data[border] = data[border], data[l]
    return border


def qs_inplace(data, l, r):
    if l < r:
        border = sort(data, l, r)
        qs_inplace(data, l, border - 1)
        qs_inplace(data, border + 1, r)


def quick_sort(data):
    qs_inplace(data, 0, len(data) - 1)


quick_sort(data)
print(data)
