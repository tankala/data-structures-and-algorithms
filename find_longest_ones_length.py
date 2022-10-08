def find_longest_ones_length(binary_array):
    longest_ones_length = 0
    before_zero_ones_length = 0
    after_zero_ones_length = 0

    for index in range(len(binary_array)):
        if binary_array[index] == 1:
            after_zero_ones_length += 1
        else:
            ones_length = before_zero_ones_length + after_zero_ones_length + 1
            longest_ones_length = max(ones_length, longest_ones_length)

            before_zero_ones_length = after_zero_ones_length
            after_zero_ones_length = 0
    
    ones_length = before_zero_ones_length + after_zero_ones_length + 1
    longest_ones_length = max(ones_length, longest_ones_length)
    
    return longest_ones_length

longest_ones_length = find_longest_ones_length(binary_array=[0,1,1,0,1,0,1,1,1])
print("Longest 1's series Length: ", longest_ones_length)