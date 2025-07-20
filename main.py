# function to open the book using a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# functino to calculate the number of words in the book
def get_num_words():
    num_words = len(get_book_text("books/frankenstein.txt").split())
    return print(f"{num_words} words found in the document")


# main function to return the printed book text
def main():
    # return print(get_book_text("books/frankenstein.txt"))
    return get_num_words()

main()
