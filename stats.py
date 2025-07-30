def get_word_count(text):
    words = text.split()
    count = len(words)
    return count
def get_char_counts(text):
    """
    Returns a dictionary with the count of each character in the text (lowercased).
    """
    lower_text = text.lower()
    char_counts = {}
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
def sorted_list(char_dict):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)