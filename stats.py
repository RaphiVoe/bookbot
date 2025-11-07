def get_num_words(string):
    words = string.split()
    return len(words)


def get_char_counts(string):
    counts = {}
    for char in string:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(items):
    return items["num"]


def get_sorted_list_of_dicts(char_dict):
    chars = []
    for char in char_dict:
        chars.append({
            'char': char,
            'num': char_dict[char]
        })
    chars.sort(reverse=True, key=sort_on)
    return chars