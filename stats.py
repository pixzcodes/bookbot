def get_num_words(book):
    word_count = book.split()
    return len(word_count)


def get_char_count(book):
    count_dict = {}

    for char in book:
        char = char.lower()
        if count_dict.get(char) is None:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict


def get_sorted_chars(char_dict):
    def sort_on(dict):
        return dict["num"]

    char_list = []
    for entry in char_dict:
        char_list.append({"name": entry, "num": char_dict[entry]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
