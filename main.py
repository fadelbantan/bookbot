from stats import get_num_words

# function to open the book using a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# main to return called function
def main():
    # return print(get_book_text("books/frankenstein.txt"))
    return print(f"{get_num_words("books/frankenstein.txt")} words found in the document")

main()
