from stats import get_word_count, get_char_counts, new_list

def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

def main():
    file = "books/frankenstein.txt"
    txt = get_book_text(file)
    word_count = get_word_count(txt)
    char_counts = get_char_counts(txt)
    final_list = new_list(char_counts)

    println("============ BOOKBOT ============")
    println(f"Analyzing book found at {file}")
    println("----------- Word Count ----------")
    println(f"Found {word_count} total words")
    println("--------- Character Count -------")
    for entry in final_list:
        println(f"{entry['char']}: {entry['num']}")
    println("============= END ===============")

main()