import sys
from stats import (
    get_num_words,
    get_char_counts,
    get_sorted_list_of_dicts
)


def get_book_text(filepath):
    file_contents = ''
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    bookpath = sys.argv[1]

    print(f"Analyzing book found at {bookpath}...")
    book_text = get_book_text(bookpath)

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words.")

    print("--------- Character Count -------")
    char_counts = get_char_counts(book_text)
    sorted_char_counts = get_sorted_list_of_dicts(char_counts)
    for char_count in sorted_char_counts:
        if not char_count["char"].isalpha():
            continue
        print(f"{char_count['char']}: {char_count['num']}")

    print("============= END ===============")


main()