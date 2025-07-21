# function to calculate the number of words in the book
def get_num_words(text):
    num_words = len(text.split())
    return num_words

# print in a dictionary each character's count
def get_char_count(text):
    char_count = {}
    
    for char in text:  # Loop through each character in the string
        lowercase_char = char.lower()  # Convert to lowercase
        char_count[lowercase_char] = char_count.get(lowercase_char, 0) + 1  # Count the occurrences
    
    return char_count

# function to return sorted list of dictionaries with character and count
def get_sorted_char_count_list(char_count):
    sorted_list = []
    
    for char, count in char_count.items():
        if char.isalpha():  # Skip non-alphabet characters
            sorted_list.append({"char": char, "num": count})
    
    # Sort the list of dictionaries by the 'num' key in descending order
    sorted_list.sort(key=lambda x: x['num'], reverse=True)
    
    return sorted_list
