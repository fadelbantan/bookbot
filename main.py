from stats import get_num_words, get_char_count

# function to open (read) the book using a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# main to return called functions
def main():
    # Get the word count
    word_count = get_num_words(get_book_text, "books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    
    # Get the character count
    char_count = get_char_count(get_book_text, "books/frankenstein.txt")
    print(f"Character counts: {char_count}")

main()
