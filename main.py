from stats import *
import sys

# function to open (read) the book using a filepath
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

# main to return called functions
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
        
    book_content = get_book_text(book_path)
    # Get the word count
    word_count = get_num_words(book_content)
    
    # Get the character count
    char_count = get_char_count(book_content)
        
    # Get the sorted list of character counts
    sorted_char_count_list = get_sorted_char_count_list(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book input...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print the sorted character counts in the desired format
    for item in sorted_char_count_list:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
