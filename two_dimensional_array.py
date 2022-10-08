two_dimensional_array = [[2, 5, 8, 12], [3, 11, 7, 6], [10, 5, 4, 8], [25, 31, 3, 6]]
print(two_dimensional_array[2][3])
two_dimensional_array[1][2] = 5

for row in two_dimensional_array:
    for element in row:
        print(element, end="\t")
    print()