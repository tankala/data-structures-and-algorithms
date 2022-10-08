def find_big_container_area(column_array):
    max_container_area = 0
    start = 0
    end = len(column_array) - 1

    while start < end:
        width = end - start
        height = min(column_array[start], column_array[end])
        area = width * height
        max_container_area = max(area, max_container_area)

        if column_array[start] < column_array[end]:
            start += 1
        else:
            end -= 1
    
    return max_container_area

big_container_area = find_big_container_area(column_array=[2, 1, 5, 8, 3, 1, 7, 2, 9])
print("Big Container Area: ", big_container_area)