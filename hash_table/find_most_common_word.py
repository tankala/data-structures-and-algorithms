def find_most_common_word(sentence):
    words = sentence.split()
    words_counter_dict = {}

    for word in words:
        count = words_counter_dict.get(word, 0)
        count += 1
        words_counter_dict[word] = count
    
    word_with_max_count = ""
    max_count = 0
    for word, count in words_counter_dict.items():
        if count > max_count:
            word_with_max_count = word
            max_count = count
    
    return word_with_max_count

print(find_most_common_word("fear leads to anger anger leads to hatred hatred leads to conflict conflict leads to suffering"))