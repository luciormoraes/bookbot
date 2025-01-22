def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    freq = get_freq(text)
    #list_of_dicts = [{"key": key, "nums": value} for key, value in freq.items() if key.isalpha()]
    #list_of_dicts.sort(reverse=True, key=sort_on)
    list_of_dicts = chars_dict_to_sorted_list(freq)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in list_of_dicts:
        if not item['key'].isalpha():
            continue
        print(f"The '{item['key']}' character was found {str(item['nums'])} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_freq(text):
    lowered_string = text.lower()
    freq = {}
    for c in set(lowered_string):
        freq[c] = lowered_string.count(c)

    return freq
    
def sort_on(dict):
    return dict["nums"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"key": ch, "nums": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
