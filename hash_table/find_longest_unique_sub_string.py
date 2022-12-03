def find_longest_unique_sub_string(word):
    character_latest_indexes_dict = {}
    longest_sub_string = ""
    window_start = 0

    for window_end, character in enumerate(word):
        character_last_appeared_index = character_latest_indexes_dict.get(character, -1)

        if character_latest_indexes_dict != -1:
            window_start = max(window_start, character_last_appeared_index + 1)
        
        if len(longest_sub_string) < (window_end - window_start):
            longest_sub_string = word[window_start:window_end + 1]
        
        character_latest_indexes_dict[character] = window_end
    
    return longest_sub_string

print(find_longest_unique_sub_string("abcdabcdfeaa"))