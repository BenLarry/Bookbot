import sys
from stats import count_words, get_book_text, count_characters, sort_dict


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    PATH = sys.argv[1]
    text = get_book_text(PATH)
    sorted_characters_values = sort_dict(count_characters(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for char in sorted_characters_values:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["value"]}")

main()
