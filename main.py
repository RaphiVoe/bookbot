from stats import get_num_words, get_char_counts


def get_book_text(filepath):
    file_contents = ''
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    print(f"Found {num_words} total words.")
    print(char_counts)


main()