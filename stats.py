# function to calculate the number of words in the book
def get_num_words(get_book_text, filepath):
    num_words = len(get_book_text(filepath).split())
    return num_words

# print in a dictionary each character's count
def get_char_count(get_book_text, filepath):
    text = tuple(get_book_text(filepath))
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        char_count[lowercase_char] = char_count.get(lowercase_char, 0) + 1
    return char_count
