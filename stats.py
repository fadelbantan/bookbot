from main import get_book_text

# functino to calculate the number of words in the book
def get_num_words():
    num_words = len(get_book_text("books/frankenstein.txt").split())
    return print(f"{num_words} words found in the document")
