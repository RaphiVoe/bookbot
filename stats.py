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