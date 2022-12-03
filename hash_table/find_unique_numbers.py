def find_unique_numbers(numbers):
    number_count_dict = {}
    for number in numbers:
        count = number_count_dict.get(number, 0)
        count += 1
        number_count_dict[number] = count
    
    unique_numbers = []
    for number, count in number_count_dict.items():
        if count == 1:
            unique_numbers.append(number)
    
    return unique_numbers

print(find_unique_numbers([1, 2, 3, 1, 4, 5, 5, 9]))