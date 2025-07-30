from stats import get_word_count, get_char_counts, sorted_list
import sys
import os

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:    
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = f"{os.getcwd()}/{sys.argv[1]}"
    txt = get_book_text(file)
    word_count = get_word_count(txt)
    char_counts = get_char_counts(txt)
    final_list = sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in final_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()