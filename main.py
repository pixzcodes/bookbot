def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

        return contents


def main():
    book = get_book_text("./books/frankenstein.txt")
    print(book)


main()
