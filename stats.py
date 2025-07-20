# function to calculate the number of words in the book
def get_num_words(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return len(book_content.split())
