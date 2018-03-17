data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def binary_search(data, item):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = round((low+high)/2)
        if data[mid] is item:
            return mid
        if data[mid] > item:
            high = mid - 1
        if data[mid] < item:
            low = mid + 1
    return None


print(binary_search(data, 14))

