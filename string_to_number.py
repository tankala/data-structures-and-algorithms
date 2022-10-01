def convert_string_to_int(number_in_string_format):
    input_string_length = len(number_in_string_format)
    sum = 0

    for character in number_in_string_format:
        number = (ord(character) - ord('A')) + 1
        place = pow(26, (input_string_length - 1))
        sum += number * place
        input_string_length -= 1
    
    print(sum)

convert_string_to_int("ABC")