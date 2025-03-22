def get_num_words(text):
    print("----------- Word Count ----------")
    return f"Found {len(text.split())} total words"

def char_count(text, char_dict):
    print("--------- Character Count -------")
    char_count_dict = {}
    report_text = ""

    for char in char_dict:
        char_count_dict[char] = text.lower().count(char)
    
    char_count_dict = sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)

    for dict in char_count_dict:
        if dict == char_count_dict[-1]:
            report_text += f"{dict[0]}: {dict[1]}"
        else:
            report_text += f"{dict[0]}: {dict[1]}\n"
    
    return report_text