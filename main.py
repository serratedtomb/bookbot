

from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main(sys_input):
    if len(sys_input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys_input[1])
    num_words = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    char_count = get_sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys_input[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
    #return num_words, char_count
main(sys.argv)