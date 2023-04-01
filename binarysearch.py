# Binary Search-(log n)

def binary_search(data, number):
    start = 0
    end = len(data) - 1
    while end - start > 1:
        mid = (end + start) // 2
        if data[mid] < number:
            start = mid + 1
        else:
            end = mid

    if data[start] == number:
        return start
    elif data[end] == number:
        return end
    else:
        return "Not Found"


print(binary_search([1, 3, 4, 5, 6], 5))
