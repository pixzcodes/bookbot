from stats import get_num_words


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

        return contents


def main():
    book = get_book_text("./books/frankenstein.txt")
    print(f'{get_num_words(book)} words found in the document')


main()
