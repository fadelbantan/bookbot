from stats import *

# function to open (read) the book using a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# main to return called functions
def main():
    # Get the word count
    word_count = get_num_words(get_book_text, "books/frankenstein.txt")
    
    # Get the character count
    char_count = get_char_count(get_book_text, "books/frankenstein.txt")
    
    # Get the sorted list of character counts
    sorted_char_count_list = get_sorted_char_count_list(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print the sorted character counts in the desired format
    for item in sorted_char_count_list:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
