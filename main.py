import sys
import os
from stats import *

# function to open (read) the book using a filepath
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

# function to list available books and let the user select one
def choose_book():
    books_dir = "books"
    if not os.path.isdir(books_dir):
        print(f"Directory '{books_dir}' not found.")
        sys.exit(1)

    books = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

    if len(books) == 0:
        print(f"No books found in '{books_dir}' directory.")
        sys.exit(1)

    print("Available books:")
    for idx, book in enumerate(books, start=1):
        print(f" {idx}. {book}")

    while True:
        choice = input("Select a book by number: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(books):
                return os.path.join(books_dir, books[index])
        except ValueError:
            pass
        print("Invalid selection. Try again.")

# main to return called functions
def main():

    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        book_path = choose_book()
        
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
