
# function to open the book using a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



# main function to return the printed book text
def main():
    return print(get_book_text("books/frankenstein.txt"))


main()
