data = [5, 3, 2, 7, 23, 12, 11, 1]
second_data = [342342,123,123, 122,12,1,5,7,3]

def bubble_sort(data):
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x] > data[y]:
                data[x], data[y] = data[y], data[x]
    return data



print(bubble_sort(data))
print(bubble_sort(second_data))