def print_in_spiral_way(two_dimensional_array):
    row_start = 0
    column_end = len(two_dimensional_array[0]) - 1
    row_end = len(two_dimensional_array) - 1
    column_start = 0

    while (row_start < row_end) and (column_start < column_end):
        for column_index in range(column_start, column_end + 1):
            print(two_dimensional_array[row_start][column_index])
        
        for row_index in range(row_start + 1, row_end + 1):
            print(two_dimensional_array[row_index][column_end])
        
        for column_index in range(column_end - 1, column_start - 1, -1):
            print(two_dimensional_array[row_end][column_index])
        
        for row_index in range(row_end - 1, row_start, -1):
            print(two_dimensional_array[row_index][column_start])
        
        row_start += 1
        row_end -= 1
        column_start += 1
        column_end -= 1

two_dimensional_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print_in_spiral_way(two_dimensional_array)