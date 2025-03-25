from stats import get_num_words, get_char_count, get_sorted_chars
from pathlib import Path

root_dir = Path(__file__).resolve().parent


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

        return contents


frankenstein_path = root_dir / "books" / "frankenstein.txt"

book = get_book_text(frankenstein_path)
char_dict = get_char_count(book)
sorted_chars = get_sorted_chars(char_dict)


def print_report():
    print("============ BOOKBOT ============")
    print('Analyzing book found at books/frankenstein.txt ...')
    print("----------- Word Count ----------")
    print(f'Found {get_num_words(book)} total words')
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item.get("name").isalpha():
            print(f'{item["name"]}: {item["num"]}')
    print("============= END ===============")


def main():
    print_report()


main()
