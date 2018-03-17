data = [1, 5, 6, 99, 4, 23, 4, 61, 34, 2, 3, 4, 6]


# Introduction to quicksort
def sum_arr(data, sum):
    length = len(data)
    if length < 2:
        return sum
    return sum_arr(data[0:length-1], sum=sum + data[length-1])


# sum_arr(data, 0)


# Quicksort
def quicksort(data):
    print(data)
    length = len(data)
    if length < 2:
        return data
    pivot = data[0]
    greater = [number for number in data if number > pivot]
    smaller = [number for number in data if number < pivot]
    return quicksort(smaller) + [pivot] + quicksort(greater)


print(quicksort(data))



